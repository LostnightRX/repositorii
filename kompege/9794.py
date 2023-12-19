with open('27_A_9794.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] >= k:
            counter += 1
print(counter)

import math
with open('27_B_9794.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
a = a[::-1]
al = 0
ans = 0
b = []
for i in a:
    if i >= k:
        ans += al
        al += 1
    elif i >= math.ceil(k/2):
        ans += al + len(b)
        b.append(i)
    else:
        ans += al
        while b and b[-1] < k-i:
            b.pop()
        ans += len(b)
print(ans)
