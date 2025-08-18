from datetime import datetime, timedelta
from typing import List, Tuple, Any
from EventHistory import Event, EventHistory
from preprocessing import load_yaml, load_all
from constraints import constraints_table
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Load log file by ID")
parser.add_argument(
    "log_id",
    nargs="?",                # makes the argument optional
    default="ExA1",           # default value if not provided
    help="ID of the log file (default: ExA1)"
)
args = parser.parse_args()

C_Table = constraints_table(args.log_id)

log_path = f"logs/{args.log_id}.xes.yaml"
example_log = load_yaml(log_path)

example_log = example_log.iloc[1:].reset_index(drop=True)

## Comment in the following if you are just interested in activity/done events. However also removes data perspective
#example_log = example_log[example_log['cpee:lifecycle:transition'] == "activity/done"].reset_index(drop=True)

def safe_eval(expr: str, context: dict) -> bool:
    try:
        return eval(expr, {}, context)
    except Exception:
        return False

def to_event(row):
    return Event(
        label=str(row['concept:name']) if row['concept:name'] is not None else "None",
        lifecycle=row['cpee:lifecycle:transition'],
        timestamp=datetime.fromisoformat(row['time:timestamp']),
        method="unknown",
        endpoint="timeout",
        dataobjects=[(d["name"], d["value"]) for d in row['data']] if row['data'] else []
    )

# --- Main verification ---
def verify_log(log: pd.DataFrame):
    E = EventHistory()
    O = {}

    possible_activities = [
        activity for expr, activity in C_Table
        if safe_eval(expr, {"E": E, "O": O})
    ]
    print(f"Before first event: possible activities → {possible_activities}")

    for idx, row in log.iterrows():
        # Convert row to Event
        event = to_event(row)
        E.add_event(event)


        if row['cpee:lifecycle:transition'] == "dataelements/change" and row['data']:
            for d in row['data']:
                name, value = d["name"], d["value"]
                O[name] = value
        
        possible_activities = [
            activity for expr, activity in C_Table
            if safe_eval(expr, {"E": E, "O": O})
        ]
        print(f"O: {O}")
        print(f"After event ({row['concept:name']}) in state {row['cpee:lifecycle:transition']}: possible activities → {possible_activities}")


verify_log(example_log)
