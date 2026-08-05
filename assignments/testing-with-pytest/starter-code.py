def add(a, b):
    return a + b


def normalize_name(name):
    return name.strip().title()


def average(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)


def is_passing(score):
    return score >= 60


# Suggested challenge:
# Write tests that cover normal behavior, edge cases, and error handling.