"""
py_iteration. Calculate function sin(x) with Taylor series
"""
import math


def sin_(value: float) -> float:
    """Calculate sin(x)"""
    calculate = 0
    for num in range(10):
        calculate += ((-1) ** num) * (value ** (2 * num + 1) / math.factorial(2 * num + 1))
    return calculate
