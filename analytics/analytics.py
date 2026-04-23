from datetime import datetime, timedelta


def get_all_habits(habits):
    return habits


def get_habits_by_periodicity(habits, periodicity):
    return [h for h in habits if h.periodicity == periodicity]


def calculate_streak(habit):
    if not habit.completions:
        return 0

    # sort completions to ensure they're in chronological order
    dates = sorted(habit.completions)

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


def get_longest_streak_all(habits):
    if not habits:
        return 0
    return max(calculate_streak(h) for h in habits)


def get_longest_streak_for_habit(habit):
    return calculate_streak(habit)
