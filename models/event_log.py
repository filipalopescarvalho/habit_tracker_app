from datetime import datetime
import uuid


class EventLog:
    VALID_STATUSES = ["completed", "missed"]

    def __init__(
        self,
        habit_id: str,
        status: str = "completed",
        completion_date=None,
        event_id=None
    ):
        if status not in self.VALID_STATUSES:
            raise ValueError("Status must be 'completed' or 'missed'.")

        self.event_id = event_id if event_id else str(uuid.uuid4())
        self.habit_id = habit_id
        self.status = status
        self.completion_date = completion_date if completion_date else datetime.now()

    def to_dict(self):
        """Convert EventLog object to dictionary for JSON storage."""
        return {
            "event_id": self.event_id,
            "habit_id": self.habit_id,
            "status": self.status,
            "completion_date": self.completion_date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        """Create EventLog object from dictionary data."""
        return cls(
            event_id=data["event_id"],
            habit_id=data["habit_id"],
            status=data["status"],
            completion_date=datetime.fromisoformat(data["completion_date"]),
        )

    def __str__(self):
        return (
            f"EventLog("
            f"event_id={self.event_id}, "
            f"habit_id={self.habit_id}, "
            f"status={self.status}, "
            f"completion_date={self.completion_date}"
            f")"
        )