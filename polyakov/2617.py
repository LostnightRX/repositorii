from itertools import accumulate as ac
with open('2617.txt') as f:
    k,n, *a = map(int, f.read().strip().split())
i = 0
res = 0
a.sort()
b = [0] + list(ac(a))
while b[i] < k:
    i += 1
res = i-1
s = b[i-1]
while s < k:
    s = s - a[i - 1] + a[i]
    i += 1
print(res, a[i-2])
