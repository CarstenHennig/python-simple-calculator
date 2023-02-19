timings = [7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98, 8.31, 9.06, 7.06, 7.67, 10.02, 6.87, 9.07]
from statistics import mean, stdev
print(mean(timings))
print(stdev(timings))

def bootstrap(data):
    return choices(data, k=len(data))

from random import choices
print(mean(bootstrap(timings)))

n = 10000
means = sorted(mean(bootstrap(timings)) for i in range(n))
print(len(means))
print(means[-20:])
print(mean(means))
print(round(n * .05))
print(means[500])
print(means[-500])
print(f'Falls in a 90% coinfidence interval froim {means[500] :.1f} to {means[-500] :.1f}')
