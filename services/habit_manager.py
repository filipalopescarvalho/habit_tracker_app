from models.habit import Habit
from models.event_log import EventLog


class HabitManager:
    def __init__(self, storage):
        self.storage = storage
        self.habits = self.storage.load_habits()
        self.events = self.storage.load_events()

    def save_habits(self):
        self.storage.save_habits(self.habits)

    def save_events(self):
        self.storage.save_events(self.events)

    def add_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self.save_habits()
        return habit

    def delete_habit(self, name):
        habit = self.get_habit_by_name(name)

        if habit:
            habit.active = False
            self.save_habits()
            return True

        return False

    def get_all_habits(self):
        return [habit for habit in self.habits if habit.active]

    def get_habit_by_name(self, name):
        for habit in self.habits:
            if habit.name == name and habit.active:
                return habit
        return None

    def complete_habit(self, name):
        habit = self.get_habit_by_name(name)

        if habit:
            event = EventLog(habit_id=habit.habit_id)
            self.events.append(event)
            self.save_events()
            return True

        return False

    def get_events_for_habit(self, habit_id):
        return [
            event for event in self.events
            if event.habit_id == habit_id
        ]

    def get_all_events(self):
        return self.events