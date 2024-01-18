from itertools import accumulate as c
with open('2623.txt') as f:
     k, n, *a = map(int, f.read().strip().split())
a.sort()
b = [0] + list(c(a))
res = 0
for i in range(len(b)):
     if b[i] > k:
          s = b[i-1]
          res = i-1
          break
g = res
while s < k:
     s -= a[g]
     g += 1
     s+= a[g]
print(res, a[g-1])
