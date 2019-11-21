"""iteration module"""
import math


def sin_(param: float) -> float:
    """calculate sin(x)"""
    result = 0
    for k in range(10):
        first_param = ((-1) ** k)
        power = 2 * k + 1
        result += first_param * (math.pow(param, power)
                                 / math.factorial(power))
    return result
