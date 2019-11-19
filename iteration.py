"""Calculates sin(x) using Taylor series"""
import math


def ser_el(var, elem):
    """Returns value of n-th element of a sine Teylor series"""
    return ((-1)**elem) * (var**(2*elem + 1))/math.factorial(2*elem + 1)


def sin_(var: float) -> float:
    """Returns sin(x) using Taylor series"""
    num_el = 7
    res = 0
    for i in range(num_el):
        res += ser_el(var, i)
        print(res)

    return res
