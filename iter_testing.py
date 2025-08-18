from datetime import datetime, timedelta
from typing import List, Tuple, Any
from EventHistory import Event, EventHistory

# --- type error protected eval of expressions ---
def safe_eval(expr: str, context: dict) -> bool:
    try:
        return eval(expr, {}, context)
    except Exception:
        return False

# --- Run tests after each event addition ---
def run_tests(E, A, B, x, y, r):
    expressions = [
        "A in E.labels()",
        "E.labels()[A][-1].timestamp - E[-1].timestamp > x",
        "A in E.labels()",
        "E[-1].label == A",
        "E.labels()[A][-1].lifecycle == 'failed'",
        "A in E.labels()",
        "E[-1].timestamp < y",
        "not A in E.labels()",
        "E.labels()[A][-1].timestamp < E.labels()[B][-1].timestamp",
        "('ar', r) in E.labels()[A].dataobjects",
        "True",
        "len(E) == 0"
    ]
    
    context = {"E": E, "A": A, "B": B, "x": x, "y": y, "r": r}
    print("=== Running Tests ===")
    for expr in expressions:
        result = safe_eval(expr, context)
        print(f"{expr}: {result}")
    print()

def test_iteratively():
    A, B = "Login", "Logout"
    r = "abc"
    x = timedelta(minutes=10)
    y = datetime(2025, 7, 22, 9, 10, 0)
    print(f'A is {A}')
    print(f'B is {B}')

    history = EventHistory()

    t0 = datetime(2025, 7, 22, 9, 0, 0)
    print(">>> Empty log")
    run_tests(history, A, B, x, y, r)

    print(">>> Add 1st event: Login (t0 + 5)")
    history.add_event(Event(
        label="Login",
        lifecycle="failed",
        timestamp=t0 + timedelta(minutes=5),
        method="POST",
        endpoint="/api/login",
        dataobjects=[("ar", r)]
    ))
    run_tests(history, A, B, x, y, r)

    print(">>> Add 2nd event: Upload (t0 + 6)")
    history.add_event(Event(
        label="Upload",
        lifecycle="start",
        timestamp=t0 + timedelta(minutes=6),
        method="PUT",
        endpoint="/api/upload",
        dataobjects=[]
    ))
    run_tests(history, A, B, x, y, r)

    print(">>> Add 3rd event: Logout (t0 + 12)")
    history.add_event(Event(
        label="Logout",
        lifecycle="end",
        timestamp=t0 + timedelta(minutes=12),
        method="POST",
        endpoint="/api/logout",
        dataobjects=[]
    ))
    run_tests(history, A, B, x, y, r)

    print(">>> Add 4th event: Login (t0 + 20) [overwrites label map for Login]")
    history.add_event(Event(
        label="Login",
        lifecycle="end",
        timestamp=t0 + timedelta(minutes=20),
        method="POST",
        endpoint="/api/login",
        dataobjects=[("ar", "not_" + r)]
    ))
    run_tests(history, A, B, x, y, r)

# --- Run everything ---
test_iteratively()

