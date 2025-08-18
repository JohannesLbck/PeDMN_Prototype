from datetime import datetime
from typing import List, Tuple, Any, Dict

class Event:
    def __init__(
        self,
        label: str,
        lifecycle: str,
        timestamp: datetime,
        method: str,
        endpoint: str,
        dataobjects: List[Tuple[str, Any]]
    ):
        self.label = label
        self.lifecycle = lifecycle
        self.timestamp = timestamp
        self.method = method
        self.endpoint = endpoint
        self.dataobjects = dataobjects

    def __repr__(self):
        return f"Event(label={self.label}, timestamp={self.timestamp.isoformat()})"


class EventHistory:
    def __init__(self):
        self.events: List[Event] = []

    def add_event(self, event: Event):
        self.events.append(event)

    def labels(self) -> Dict[str, List[Event]]:
        """Returns a dict mapping each label to a list of all events with that label."""
        label_map: Dict[str, List[Event]] = {}
        for event in self.events:
            label_map.setdefault(event.label, []).append(event)
        return label_map

    def filter_by_label(self, label: str) -> List[Event]:
        return [event for event in self.events if event.label == label]

    def __len__(self):
        return len(self.events)

    def __getitem__(self, index: int) -> Event:
        return self.events[index]

    def __repr__(self):
        return f"EventHistory({len(self.events)} events)"
