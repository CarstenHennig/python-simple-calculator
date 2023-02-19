import itertools
import math
from typing import Tuple
from itertools import *
from pprint import pprint


def quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
    """ Compute the two roots of the quadratic expression
        ax**2 + bx + c = 0
        Written in Python as:
        a*x**2 + b*x + c == 0
    """
    discriminant = math.sqrt(b ** 2.0 - 4.0 * a * c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2


def test_quadratic():
    x1, x2 = quadratic(a=8, b=22, c=15)
    assert 8 * x1 ** 2 + 22 * x1 + 15 == 0
    assert 8 * x2 ** 2 + 22 * x2 + 15 == 0


def test_quadratic_types():
    quadratic(a=8, b=22, c=15)


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())

test_quadratic()
test_quadratic_types()

for t in product('ABC', 'DE', 'xyz'):
    pprint(t)
for t in permutations('LOVE', 2):
    pprint(t)


def test_torture_test():
    args = [10, 0, 1, 18, -5, -1, 0.5, -1.5]
    for i in itertools.permutations(args, 3):
        x1, x2 = quadratic(*i)


test_torture_test()
