from models.habit import Habit
from models.event_log import EventLog


class HabitManager:
    ### Manages habits and their completion events. Provides methods to add, delete, and complete habits,
    def __init__(self, storage):
        self.storage = storage
        self.habits = self.storage.load_habits()
        self.events = self.storage.load_events()

    def save_habits(self):
        self.storage.save_habits(self.habits)

    def save_events(self):
        self.storage.save_events(self.events)

    def add_habit(self, name, periodicity):
        ### Add a new habit with the given name and periodicity (daily or weekly).
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self.save_habits()
        return habit

    def delete_habit(self, name):
        ### Mark a habit as inactive (soft delete) by name. Returns True if the habit was found and marked as inactive, False otherwise.
        habit = self.get_habit_by_name(name)

        if habit:
            habit.active = False
            self.save_habits()
            return True

        return False

    def get_all_habits(self):
        ### Return a list of all active habits.
        return [
            habit for habit in self.habits
            if habit.active
        ]

    def get_habit_by_name(self, name):
        ### Return a habit object by its name if it exists and is active, otherwise return None. 
        for habit in self.habits:
            if habit.name == name and habit.active:
                return habit
        return None

    def complete_habit(self, name):
        ### Mark a habit as completed.

        habit = self.get_habit_by_name(name)

        if habit:
            habit.add_completion()
            self.save_habits()
            return True

        return False

    def get_habit_completion_count(self, habit_id):
        return len([
            event for event in self.events
            if event.habit_id == habit_id
            and event.status == "completed"
        ])

    def get_events_for_habit(self, habit_id):
        return [
            event for event in self.events
            if event.habit_id == habit_id
        ]

    def get_all_events(self):
        return self.events