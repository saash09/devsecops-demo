# This file intentionally violates SonarCloud rules

def calculate_sum(a, b):
    # BUG: wrong calculation
    return a - b   # Should be a + b

def unused_function():
    # TODO: Remove this unused function
    pass

