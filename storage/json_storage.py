import json

from models.habit import Habit
from models.event_log import EventLog

### JSONStorage class to handle saving and loading habits and events to/from JSON files.

class JSONStorage:
    def __init__(
        self,
        habits_file="habits.json",
        events_file="events.json"
    ):
        self.habits_file = habits_file
        self.events_file = events_file



    def save_habits(self, habits):
        with open(self.habits_file, "w") as file:
            json.dump(
                [habit.to_dict() for habit in habits],
                file,
                indent=4
            )

    def load_habits(self):
        try:
            with open(self.habits_file, "r") as file:
                data = json.load(file)
                return [Habit.from_dict(item) for item in data]

        except FileNotFoundError:
            return []

   
    def save_events(self, events):
        with open(self.events_file, "w") as file:
            json.dump(
                [event.to_dict() for event in events],
                file,
                indent=4
            )

    def load_events(self):
        try:
            with open(self.events_file, "r") as file:
                data = json.load(file)
                return [EventLog.from_dict(item) for item in data]

        except FileNotFoundError:
            return []