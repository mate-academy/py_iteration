"""module sin"""
import math


def sin_(xarg: float) -> float:
    """sinus taylor"""
    res = 0.0
    for count in range(1, 10):
        res = res + (math.pow(-1, count-1) *
                     ((math.pow(xarg, 2 * count - 1))/(math.factorial(2*count-1))))
    print(res)
    return res
