"""module sinx"""
import math


def sin_(sin_x: float) -> float:
    """function sinx"""
    result = 0.0
    number = 3
    for index in range(15):
        if not index:
            result += sin_x
        elif index % 2 != 0:
            result -= (sin_x ** number) / (math.factorial(number))
            number += 2
        else:
            result += (sin_x ** number) / (math.factorial(number))
            number += 2

    return result
