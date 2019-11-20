"""Calculation function sin(x) with Taylor series"""
import math


def sin_(x: float) -> float:
    """Result method for calculation sin(x) with Taylor series"""
    order = 10
    result = 0
    for i in range(order):
        result += ((-1) ** i) * (x ** (2 * i + 1) / math.factorial(2 * i + 1))
    return result
