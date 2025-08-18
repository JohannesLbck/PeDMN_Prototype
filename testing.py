from datetime import datetime, timedelta
from typing import List, Tuple, Any
from EventHistory import Event, EventHistory

# Sample setup
A = "UserLogin"
B = "UserLogout"
r = "some_value"
x = timedelta(minutes=10)
y = datetime(2025, 7, 22, 9, 10, 0)


# Create EventHistory
history = EventHistory()

t0 = datetime(2025, 7, 22, 9, 0, 0)
t1 = t0 + timedelta(minutes=5)
t2 = t0 + timedelta(minutes=15)

history.add_event(Event(
    label=A,
    lifecycle="failed",
    timestamp=t1,
    method="POST",
    endpoint="/api/login",
    dataobjects=[("ar", r)]
))

history.add_event(Event(
    label=B,
    lifecycle="end",
    timestamp=t2,
    method="POST",
    endpoint="/api/logout",
    dataobjects=[]
))

# Assign to E
E = history

# Direct usage in all expressions
print(f"A in E.labels(): {A in E.labels()}")
print(f"E.labels()[A][-1].timestamp - E[-1].timestamp > x: {(E.labels()[A][-1].timestamp - E[-1].timestamp) > x}")
print(f"A in E.labels(): {A in E.labels()}")
print(f"E[-1].label == A: {E[-1].label == A}")
print(f"E.labels()[A][-1].lifecycle == 'failed': {E.labels()[A][-1].lifecycle == 'failed'}")
print(f"A in E.labels(): {A in E.labels()}")
print(f"E[-1].timestamp < y: {E[-1].timestamp < y}")
print(f"not A in E.labels(): {not A in E.labels()}")
print(f"E.labels()[A][-1].timestamp < E.labels()[B][-1].timestamp: {E.labels()[A][-1].timestamp < E.labels()[B][-1].timestamp}")
print(f"E.labels()[A][-1].dataobjects contains ('ar', r): {('ar', r) in E.labels()[A][-1].dataobjects}")
print(f"TRUE: {True}")
E_empty = EventHistory()
print(f"len(E_empty) == 0: {len(E_empty) == 0}")
print(E[0])
