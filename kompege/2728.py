with open('27A_2728.txt') as f:
     n = int(f.readline())
     a = [int(x) for x in f.readlines()]
res = 0
for i in range(n):
     for j in range(i+1, n):
          if (a[i] + a[j]) % 2 == 0 and(a[i] %23 == 0 or a[j] % 23 == 0):
               res = max(res, a[i] + a[j])
print(res)

res = 0

with open('27B_2728.txt') as f:
     n = int(f.readline())
     a = [int(x) for x in f.readlines()]
d = []
b = list(map(lambda x: x*(x % 23 == 0 and x % 2 == 0), a))
c = list(map(lambda x: x*(x % 2 == 0), a))

b1 = list(map(lambda x: x*(x % 23 == 0 and x % 2 != 0), a))
c1 = list(map(lambda x: x*(x % 2 != 0), a))

print(max(max(b) + max(c), max(b1) + max(c1)))
