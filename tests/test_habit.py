import pytest # type: ignore
from models.habit import Habit


def test_create_daily_habit():
    habit = Habit("Drink water", "daily")

    assert habit.name == "Drink water"
    assert habit.periodicity == "daily"
    assert habit.active is True


def test_invalid_periodicity():
    with pytest.raises(ValueError):
        Habit("Read book", "monthly")