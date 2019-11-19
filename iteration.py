"""math for pi"""
import math


def sin_(angle: float) -> float:
    """calculate sin"""
    result = 0
    for i in range(10):
        first = (-1) ** i
        result += first * (angle ** (2 * i + 1) / math.factorial(2 * i + 1))
    return result
