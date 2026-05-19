from services.habit_manager import HabitManager
from storage.json_storage import JSONStorage


def test_add_habit():
    storage = JSONStorage(
        habits_file="test_habits.json",
        events_file="test_events.json"
    )

    manager = HabitManager(storage)

    initial_count = len(manager.get_all_habits())

    manager.add_habit("Test Habit", "daily")

    assert len(manager.get_all_habits()) == initial_count + 1


def test_complete_habit():
    storage = JSONStorage(
        habits_file="test_habits.json",
        events_file="test_events.json"
    )

    manager = HabitManager(storage)

    manager.add_habit("Workout", "weekly")

    manager.complete_habit("Workout")

    habit = manager.get_habit_by_name("Workout")

    assert len(habit.completions) == 1


def test_delete_habit():
    storage = JSONStorage(
        habits_file="test_habits.json",
        events_file="test_events.json"
    )

    manager = HabitManager(storage)

    manager.add_habit("Meditation", "daily")

    manager.delete_habit("Meditation")

    habit = manager.get_habit_by_name("Meditation")

    assert habit is None