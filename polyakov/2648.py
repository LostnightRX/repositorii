import math
with open('2648.txt') as f:
     n, *a = map(int, f.readlines())
b = []
res = 0
g = 0
for i in a:
     if i > 100:
          b.append(i)
     else:
          res += i
b.sort()
l = 0
r = len(b)-1
arg = 1
while l <= r:
     arg += 1
     arg %= 2
     if arg:
          g = b[l]
          res += b[l] * 0.9
          l+=1
     else:
          res += b[r]
          r -= 1
print(math.ceil(res), g)
