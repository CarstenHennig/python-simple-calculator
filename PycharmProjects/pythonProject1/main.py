
import pprint
from collections import defaultdict
names = ''' david betty susan simon michael mary harry tom beatrice hillard tim doris '''.split()
d = defaultdict(list)
for name in names:
    feature = len(name)
    d[feature].append(name)

print(sorted(names, key=len))

from itertools import zip_longest
print(list(zip_longest('abcdef', 'ghijklm', fillvalue='X')))

m = [
    [10,20],
    [30,40],
    [50,60]
]
print(list(zip(*m)))

for row in m:
    for col in row:
        print(col)

pprint([x for row in m for x in row])

