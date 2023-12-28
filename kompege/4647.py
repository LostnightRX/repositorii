import math
from itertools import accumulate
with open('27B_4647.txt') as f:
     n, k, *a = map(int, f.read().strip().split())
b = list(map(lambda x: math.ceil(x/6), a))
c = [0]+list(accumulate(b))
s0 = s1 = s2 = 0
for i in range(4*k + 3, len(c)):
     s1 = c[i - 2*k - 2] - c[i-4*k - 3]
     s0 = max(s0, s1)
     s2 = max(s2, (s0 + c[i] - c[i - 2*k - 1]))
print(s2)
