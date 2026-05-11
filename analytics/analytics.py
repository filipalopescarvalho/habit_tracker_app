from datetime import timedelta


def get_all_habits(habits):
    return habits


def get_habits_by_periodicity(habits, periodicity):
    return [
        habit for habit in habits
        if habit.periodicity == periodicity
    ]


def get_events_for_habit(events, habit_id):
    return [
        event for event in events
        if event.habit_id == habit_id and event.status == "completed"
    ]


def calculate_streak(events, habit):
    habit_events = get_events_for_habit(events, habit.habit_id)

    if not habit_events:
        return 0

    dates = sorted(
        event.completion_date
        for event in habit_events
    )

    streak = 1
    max_streak = 1

    for i in range(1, len(dates)):
        diff = dates[i] - dates[i - 1]

        if habit.periodicity == "daily":
            if diff <= timedelta(days=1):
                streak += 1
            else:
                streak = 1

        elif habit.periodicity == "weekly":
            if diff <= timedelta(days=7):
                streak += 1
            else:
                streak = 1

        max_streak = max(max_streak, streak)

    return max_streak


def get_longest_streak_all(habits, events):
    if not habits:
        return 0

    return max(
        calculate_streak(events, habit)
        for habit in habits
    )


def get_longest_streak_for_habit(habit, events):
    return calculate_streak(events, habit)


def calculate_success_rate(events, habit):
    habit_events = get_events_for_habit(events, habit.habit_id)

    if not habit_events:
        return 0

    completed_events = [
        event for event in habit_events
        if event.status == "completed"
    ]

    return len(completed_events) / len(habit_events)