import json
from models.habit import Habit


class JSONStorage:
    def __init__(self, filename):
        self.filename = filename

    def save_habits(self, habits):
        with open(self.filename, "w") as file:
            json.dump([habit.to_dict() for habit in habits], file, indent=4)

    def load_habits(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Habit.from_dict(item) for item in data]
        except FileNotFoundError:
            return []