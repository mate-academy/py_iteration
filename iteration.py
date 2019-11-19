""" module docstring """
import math


def sin_(number):
    """ function docstring """
    sine = 0
    i = 0
    while True:
        max_sine = sine
        sine += ((-1) ** (i)) * ((number ** (2 * i + 1))
                                 / math.factorial(2 * i + 1))
        if (max_sine - sine) < 1e-10:
            break
        max_sine = sine

    return sine
