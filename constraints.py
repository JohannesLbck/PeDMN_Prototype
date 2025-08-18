# Constraint tables
C_Table_A = [
        ("'A' in E.labels() and not 'B' in E.labels()", "B"),
        ("len(E) == 0","A"),
        ("E[-1].label == 'E' and E[-1].lifecycle == 'activity/done'","end"),
        ("E[-1].label == 'A'", "C"),
        ("'B' in E.labels() and O['object']", "E"),
        ("not 'D' in E.labels() and 'B' in E.labels() and not O['object']", "D"),
        ("E[-1].label == 'D' and E[-1].lifecycle == 'activity/done'", "end")
        ]

C_Table_B = [
        ("len(E) == 0", "A"),
        ("O['o'] == 'consider'", "B"),
        ("O['o'] == 'deny' and not 'C' in E.labels() ","C"),
        ("E[-1].label == 'C' and E[-1].lifecycle == 'activity/done'","end"),
        ("O['o'] == 'accept' and not 'D' in E.labels()", "D"),
        ("'D' in E.labels() and not 'E' in E.labels()","E"),
        ("E[-1].label == 'E' and E[-1].lifecycle == 'activity/done'","end"),
        ]
C_Table_C = [
        ('not "A" in E.labels()', 'A'),
        ('E[-1].label == "B" and O["o1"]', 'A'),
        ('E[-1].label == "A"', 'B'),
        ('not "C" in E.labels() and O["o2"]', 'C'),
        ("O['o2'] and E[-1].label == 'C' and E[-1].lifecycle == 'activity/done'","end"),
        ("not O['o2'] and not O['o1] and E[-1].label == 'C' and E[-1].lifecycle == 'activity/done'","end"),
        ]
C_Table_D = [
        ( "len(E) == 0", "('A', 'B')"),
        ("O['o1'] and not 'C' in E.labels()", "C"),
        ("O['o2'] and not 'D' in E.labels()", "D"),
        ("O['o1'] and O['o2'] and not 'C' in E.labels() and not 'D' in E.labels()", "('C', 'D')"),
        ("E[-1].label == 'D' and E[-1].lifecycle == 'activity/done'","end"),
        ("O['o1'] and E[-1].label == 'C' and E[-1].lifecycle == 'activity/done'","end"),
        ]
C_Table_E = [
        ("len(E) == 0", "A"),
        ("len(E) == 0", "B"),
        ("'A' in E.labels() and not 'C' in E.labels()", "C"),
        ("'B' in E.labels() and not 'D' in E.labels()", "D"),
        ("O['o2'] and not 'E' in E.labels()", "E"),
        ("not O['o2'] and E[-1].label == 'C' and E[-1].lifecycle == 'activity/done'","end"),
        ("O['o2'] and E[-1].label == 'E' and E[-1].lifecycle == 'activity/done'","end"),
        ("not O['o2'] and E[-1].label == 'D' and E[-1].lifecycle == 'activity/done'","end"),
        ]


# Mapping from log id to table
TABLE_MAP = {
    "ExA": C_Table_A,
    "ExB": C_Table_B,
    "ExC": C_Table_C,
    "ExD": C_Table_D,
    "ExE": C_Table_E,
}

def constraints_table(log_id: str):
    """Return the decision table mapping to the log ID."""
    for prefix, table in TABLE_MAP.items():
        if log_id.startswith(prefix):
            return table
    return None
