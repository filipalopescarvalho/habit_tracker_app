from datetime import datetime, timedelta

from models.habit import Habit
from models.event_log import EventLog
from analytics.analytics import calculate_streak


def test_daily_streak():
    habit = Habit("Exercise", "daily", habit_id="habit-1")

    base_date = datetime(2026, 5, 1)

    events = [
        EventLog("habit-1", completion_date=base_date - timedelta(days=2)),
        EventLog("habit-1", completion_date=base_date - timedelta(days=1)),
        EventLog("habit-1", completion_date=base_date),
    ]

    assert calculate_streak(events, habit) == 3