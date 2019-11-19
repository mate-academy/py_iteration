"""
module for calculation function sin(x) with Taylor series
"""

import math


def sin_(num: float) -> float:
    """
    Calculate sin(x) with Taylor series
    :param num: float
    :return: float
    """
    e_degree = 2
    e_to_2 = 0
    for i in range(int(num)):
        e_to_2 += e_degree ** i / math.factorial(i)

    return e_to_2

