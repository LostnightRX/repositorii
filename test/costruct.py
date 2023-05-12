import random
from itertools import product
a = [int(random.random() * 100) for _ in range(6)]
a1 = ''
for i in range(len(a)):
    a1 += str(a[i])
#1
for i in a:
    print(f'good {i}')
for i in range(len(a)):
    print(f'bad {a[i]}')

combo = []
#2
for i in range(len(a)):
    for j in range(len(a)):
        combo.append(f'{i, j}')
print(len(combo))

combo0 = product(a1, repeat = 2)
combo0 = list(combo0)
print(f'это количество комбинаций - {len(combo0)}')


#3
for i, j in enumerate(combo):
    x = list(j)
    if x[0] == x[1]:
        combo.pop(i)
print(len(combo))

for i in a:
    h = [str(i), str(i)]
    while combo0.count(h) > 0:
        combo0.pop(combo0.index(h))
print(len(combo0))

#4
for r in range(1, len(a)):
    for l in range(len(a) - 1):
        if a[l] > a[r]:
            a[l], a[r] = a[r], a[l]
print(a)
