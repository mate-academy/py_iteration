"""
docstring
"""
import math


def sin_(ang: float) -> float:
    """

    :param ang:
    :return:
    """
    sin_ang = 0
    for i in range(10):
        sin_ang += (-1) ** i * (ang ** (2 * i + 1) / math.factorial(2 * i + 1))
    return sin_ang
