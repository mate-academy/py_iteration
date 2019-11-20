"""Calculates sin(x)"""
import math


def sin_(param: float) -> float:
    """Calculates sin(x)"""
    result = 0
    for i in range(10):
        first = (-1) ** i
        result += first * (param ** (2 * i + 1) / math.factorial(2 * i + 1))
    return result
