from services.habit_manager import HabitManager
from storage.json_storage import JSONStorage
from analytics.analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak_all,
    get_longest_streak_for_habit,
    calculate_success_rate,
)


def print_habit_with_completion_count(manager, habit):
    completion_count = manager.get_habit_completion_count(habit.habit_id)

    print(
        f"Habit("
        f"id={habit.habit_id}, "
        f"name={habit.name}, "
        f"periodicity={habit.periodicity}, "
        f"completions={completion_count}"
        f")"
    )


def run_cli():
    storage = JSONStorage(
        habits_file="habits.json",
        events_file="events.json"
    )
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
        print("8. Show success rate (one habit)")
        print("9. Delete habit")
        print("10. Exit")

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
            habits = get_all_habits(manager.get_all_habits())

            if not habits:
                print("No habits found.")
            else:
                for habit in habits:
                    print_habit_with_completion_count(manager, habit)

        elif choice == "4":
            daily_habits = get_habits_by_periodicity(
                manager.get_all_habits(),
                "daily"
            )

            if not daily_habits:
                print("No daily habits found.")
            else:
                for habit in daily_habits:
                    print_habit_with_completion_count(manager, habit)

        elif choice == "5":
            weekly_habits = get_habits_by_periodicity(
                manager.get_all_habits(),
                "weekly"
            )

            if not weekly_habits:
                print("No weekly habits found.")
            else:
                for habit in weekly_habits:
                    print_habit_with_completion_count(manager, habit)

        elif choice == "6":
            longest_streak = get_longest_streak_all(
                manager.get_all_habits(),
                manager.get_all_events()
            )

            print("Longest streak:", longest_streak)

        elif choice == "7":
            name = input("Habit name: ")
            habit = manager.get_habit_by_name(name)

            if habit:
                longest_streak = get_longest_streak_for_habit(
                    habit,
                    manager.get_all_events()
                )
                print("Longest streak:", longest_streak)
            else:
                print("Habit not found.")

        elif choice == "8":
            name = input("Habit name: ")
            habit = manager.get_habit_by_name(name)

            if habit:
                success_rate = calculate_success_rate(
                    manager.get_all_events(),
                    habit
                )
                print(f"Success rate: {success_rate:.2%}")
            else:
                print("Habit not found.")

        elif choice == "9":
            name = input("Habit name: ")

            if manager.delete_habit(name):
                print("Habit deleted.")
            else:
                print("Habit not found.")

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")