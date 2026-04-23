from models.habit import Habit


class HabitManager:
    def __init__(self, storage):
        self.storage = storage
        self.habits = self.storage.load_habits()

    def save(self):
        self.storage.save_habits(self.habits)

    def add_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self.save()
        return habit

    def delete_habit(self, name):
        self.habits = [h for h in self.habits if h.name != name]
        self.save()

    def get_all_habits(self):
        return self.habits

    def get_habit_by_name(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def complete_habit(self, name):
        habit = self.get_habit_by_name(name)
        if habit:
            habit.add_completion()
            self.save()
            return True
        return False