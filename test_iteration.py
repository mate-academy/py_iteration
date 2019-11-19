'''Test module'''
import math

import iteration


def test_0():
    '''test1'''
    assert math.isclose(iteration.sin_(0), 0)


def test_pi_2():
    '''test2'''
    assert math.isclose(iteration.sin_(math.pi/2), 1)


def test_pi_6():
    '''test3'''
    assert math.isclose(iteration.sin_(math.pi/6), 0.5)
