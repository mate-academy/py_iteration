'''Module'''
import math


def sin_(degree: float) -> float:
    '''Result def'''
    answer = 0
    for i in range(10):
        answer += ((-1) ** i) * (degree ** (2 * i + 1) / math.factorial(2 * i + 1))
    return answer
