from datetime import datetime


class Habit:
    VALID_PERIODICITIES = ["daily", "weekly"]

    def __init__(self, name: str, periodicity: str, created_at=None, completions=None):
        if periodicity not in self.VALID_PERIODICITIES:
            raise ValueError("Periodicity must be 'daily' or 'weekly'.")

        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at if created_at else datetime.now()
        self.completions = completions if completions else []

    def add_completion(self):
        """Record a completion with the current timestamp."""
        self.completions.append(datetime.now())

    def to_dict(self):
        """Convert Habit object to dictionary for JSON storage."""
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [completion.isoformat() for completion in self.completions],
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Habit object from dictionary data."""
        return cls(
            name=data["name"],
            periodicity=data["periodicity"],
            created_at=datetime.fromisoformat(data["created_at"]),
            completions=[datetime.fromisoformat(c) for c in data["completions"]],
        )

    def __str__(self):
        return f"Habit(name={self.name}, periodicity={self.periodicity}, completions={len(self.completions)})"