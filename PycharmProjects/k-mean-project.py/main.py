from pprint import pprint
from math import fsum, hypot, sqrt
from typing import Iterable

Point = Tuple[int, ...]

points = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12),
    (21, 36, 23),
]

def mean(data: Iterable[float]) -> float:
    data = list(data)
    pprint(fsum(data) / len(data))

mean([10, 20, 61])

pprint(hypot(3,4))

def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip):
    pprint(sqrt(fsum((x - y)**2 for x, y in zip(p, q))))


