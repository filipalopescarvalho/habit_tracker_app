from services.habit_manager import HabitManager
from storage.json_storage import JSONStorage
from analytics.analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak_all,
    get_longest_streak_for_habit
)


def run_cli():
    storage = JSONStorage("habits.json")
    manager = HabitManager(storage)

    while True:
        print("\n--- Habit Tracker ---")
        print("1. Create habit")
        print("2. Complete habit")
        print("3. Show all habits")
        print("4. Show daily habits")
        print("5. Show weekly habits")
        print("6. Show longest streak (all)")
        print("7. Show longest streak (one habit)")
        print("8. Delete habit")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Habit name: ")
            periodicity = input("Periodicity (daily/weekly): ")
            try:
                manager.add_habit(name, periodicity)
                print("Habit added.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            name = input("Habit name: ")
            if manager.complete_habit(name):
                print("Habit completed.")
            else:
                print("Habit not found.")

        elif choice == "3":
            for h in get_all_habits(manager.get_all_habits()):
                print(h)

        elif choice == "4":
            for h in get_habits_by_periodicity(manager.get_all_habits(), "daily"):
                print(h)

        elif choice == "5":
            for h in get_habits_by_periodicity(manager.get_all_habits(), "weekly"):
                print(h)

        elif choice == "6":
            print("Longest streak:", get_longest_streak_all(manager.get_all_habits()))

        elif choice == "7":
            name = input("Habit name: ")
            habit = manager.get_habit_by_name(name)
            if habit:
                print("Longest streak:", get_longest_streak_for_habit(habit))
            else:
                print("Habit not found.")

        elif choice == "8":
            name = input("Habit name: ")
            manager.delete_habit(name)
            print("Habit deleted.")

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")