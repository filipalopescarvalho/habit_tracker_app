from models.event_log import EventLog


def test_create_event_log():
    event = EventLog(habit_id="habit-123")

    assert event.habit_id == "habit-123"
    assert event.status == "completed"
    assert event.event_id is not None
    assert event.completion_date is not None