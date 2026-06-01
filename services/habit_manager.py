from models.habit import Habit
from models.event_log import EventLog


class HabitManager:
    """Manages habits and their completion events."""

    def __init__(self, storage):
        self.storage = storage
        self.habits = self.storage.load_habits()
        self.events = self.storage.load_events()

    def save_habits(self):
        """Save habits to storage."""
        self.storage.save_habits(self.habits)

    def save_events(self):
        """Save events to storage."""
        self.storage.save_events(self.events)

    def add_habit(self, name, periodicity):
        """Add a new habit with the given name and periodicity."""
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self.save_habits()
        return habit

    def delete_habit(self, name):
        """Mark a habit as inactive by name."""
        habit = self.get_habit_by_name(name)

        if habit:
            habit.active = False
            self.save_habits()
            return True

        return False

    def get_all_habits(self):
        """Return all active habits."""
        return [habit for habit in self.habits if habit.active]

    def get_habit_by_name(self, name):
        """Return an active habit by name."""
        for habit in self.habits:
            if habit.name == name and habit.active:
                return habit
        return None

    def complete_habit(self, name):
        """Mark a habit as completed and create an event log entry."""
        habit = self.get_habit_by_name(name)

        if habit:
            habit.add_completion()

            event = EventLog(habit_id=habit.habit_id)
            self.events.append(event)

            self.save_habits()
            self.save_events()

            return True

        return False

    def get_habit_completion_count(self, habit_id):
        """Return the number of completed events for a habit."""
        return len([
            event for event in self.events
            if event.habit_id == habit_id and event.status == "completed"
        ])

    def get_events_for_habit(self, habit_id):
        """Return all events for a specific habit."""
        return [
            event for event in self.events
            if event.habit_id == habit_id
        ]

    def get_all_events(self):
        """Return all stored events."""
        return self.events