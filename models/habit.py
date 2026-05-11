from datetime import datetime
import uuid


class Habit:
    VALID_PERIODICITIES = ["daily", "weekly"]

    def __init__(
        self,
        name: str,
        periodicity: str,
        created_at=None,
        completions=None,
        habit_id=None,
        active=True
    ):

        if periodicity not in self.VALID_PERIODICITIES:
            raise ValueError("Periodicity must be 'daily' or 'weekly'.")

        self.habit_id = habit_id if habit_id else str(uuid.uuid4())
        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at if created_at else datetime.now()
        self.completions = completions if completions else []
        self.active = active

    def add_completion(self):
        """Record a completion with the current timestamp."""
        self.completions.append(datetime.now())

    def to_dict(self):
        """Convert Habit object to dictionary for JSON storage."""
        return {
            "habit_id": self.habit_id,
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [c.isoformat() for c in self.completions],
            "active": self.active,
        }

    @classmethod
    def from_dict(cls, data):
        """Create Habit object from dictionary."""
        return cls(
            habit_id=data["habit_id"],
            name=data["name"],
            periodicity=data["periodicity"],
            created_at=datetime.fromisoformat(data["created_at"]),
            completions=[
                datetime.fromisoformat(c)
                for c in data["completions"]
            ],
            active=data.get("active", True)
        )

    def __str__(self):
        return (
            f"Habit("
            f"id={self.habit_id}, "
            f"name={self.name}, "
            f"periodicity={self.periodicity}, "
            f"completions={len(self.completions)}"
            f")"
        )