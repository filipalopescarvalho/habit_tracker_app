from datetime import datetime, timedelta

from cli import run_cli
from storage.json_storage import JSONStorage
from services.habit_manager import HabitManager
from models.event_log import EventLog


def generate_daily_events(habit_id, completed_days):
    events = []
    today = datetime.now()

    for day_offset in completed_days:
        completion_date = today - timedelta(days=day_offset)
        events.append(
            EventLog(
                habit_id=habit_id,
                completion_date=completion_date,
                status="completed"
            )
        )

    return events


def generate_weekly_events(habit_id, completed_weeks):
    events = []
    today = datetime.now()

    for week_offset in completed_weeks:
        completion_date = today - timedelta(weeks=week_offset)
        events.append(
            EventLog(
                habit_id=habit_id,
                completion_date=completion_date,
                status="completed"
            )
        )

    return events


def setup_initial_data():
    storage = JSONStorage(
        habits_file="habits.json",
        events_file="events.json"
    )
    manager = HabitManager(storage)

    if not manager.get_all_habits():
        created_date = datetime.now() - timedelta(days=28)

        drink_water = manager.add_habit("Drink Water", "daily")
        make_bed = manager.add_habit("Make Bed", "daily")
        read = manager.add_habit("Read", "daily")
        journal = manager.add_habit("Journal", "daily")
        exercise = manager.add_habit("Exercise", "weekly")

        for habit in [drink_water, make_bed, read, journal, exercise]:
            habit.created_at = created_date

        manager.save_habits()

        events = []

        events.extend(
            generate_daily_events(
                drink_water.habit_id,
                [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27]
            )
        )

        events.extend(
            generate_daily_events(
                make_bed.habit_id,
                [0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 23, 24, 25, 27]
            )
        )

        events.extend(
            generate_daily_events(
                read.habit_id,
                [0, 2, 3, 5, 6, 8, 10, 11, 13, 14, 17, 18, 20, 22, 24, 25, 27]
            )
        )

        events.extend(
            generate_daily_events(
                journal.habit_id,
                [1, 3, 4, 7, 9, 12, 13, 16, 19, 21, 22, 26]
            )
        )

        events.extend(
            generate_weekly_events(
                exercise.habit_id,
                [0, 1, 2, 3]
            )
        )

        manager.events.extend(events)
        manager.save_events()


if __name__ == "__main__":
    setup_initial_data()
    run_cli()