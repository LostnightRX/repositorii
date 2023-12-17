with open('27A_2724.txt') as f:
     n = int(f.readline())
     a = [int(x) for x in f.readlines()]
res = 0
for i in range(len(a)):
     for j in range(i + 1, len(a)):
          if (a[i] + a[j]) % 131 == 0:
               res += 1
print(res)

res = 0

with open('27B_2724.txt') as f:
     n = int(f.readline())
     a = [int(x) for x in f.readlines()]
b = list(map(lambda x: x % 131, a))
for x,i in enumerate(b):
     if i == 0:
          res += b[x + 1:].count(0)
     else:
          res += b[x + 1:].count(131 - i)
print(res)
