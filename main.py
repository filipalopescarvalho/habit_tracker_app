from datetime import datetime, timedelta

from cli import run_cli
from storage.json_storage import JSONStorage
from services.habit_manager import HabitManager


def generate_daily_completions(days_back, completed_days):
    completions = []
    today = datetime.now()

    for day_offset in completed_days:
        completion_date = today - timedelta(days=day_offset)
        completions.append(completion_date)

    return completions


def generate_weekly_completions(weeks_back, completed_weeks):
    completions = []
    today = datetime.now()

    for week_offset in completed_weeks:
        completion_date = today - timedelta(weeks=week_offset)
        completions.append(completion_date)

    return completions


def setup_initial_data():
    storage = JSONStorage("habits.json")
    manager = HabitManager(storage)

    if not manager.get_all_habits():
        
        created_date = datetime.now() - timedelta(days=28)

        # Create sample habits with varying consistency
        drink_water = manager.add_habit("Drink Water", "daily")
        make_bed = manager.add_habit("Make Bed", "daily")
        read = manager.add_habit("Read", "daily")
        journal = manager.add_habit("Journal", "daily")
        exercise = manager.add_habit("Exercise", "weekly")

        # Set consistent creation date for all habits
        drink_water.created_at = created_date
        make_bed.created_at = created_date
        read.created_at = created_date
        journal.created_at = created_date
        exercise.created_at = created_date


        # Drink Water: very consistent, only a few missed days
        drink_water.completions = generate_daily_completions(
            28, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27]
        )

        # Make Bed: mostly consistent, a few missed days
        make_bed.completions = generate_daily_completions(
            28, [0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 23, 24, 25, 27]
        )

        # Read: moderate consistency, some missed days
        read.completions = generate_daily_completions(
            28, [0, 2, 3, 5, 6, 8, 10, 11, 13, 14, 17, 18, 20, 22, 24, 25, 27]
        )

        # Journal: less consistent, more sporadic
        journal.completions = generate_daily_completions(
            28, [1, 3, 4, 7, 9, 12, 13, 16, 19, 21, 22, 26]
        )

        # Exercise: weekly habit with some consistency
        exercise.completions = generate_weekly_completions(
            4, [0, 1, 2, 3]
        )

        # Save habits to storage
        manager.save()


if __name__ == "__main__":
    setup_initial_data()
    run_cli()