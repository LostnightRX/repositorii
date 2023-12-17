with open('27_A_10108.txt') as f:
     k = int(f.readline())
     n = f.readline()
     a = [int(x) for x in f.readlines()]
res = 0
for i in range(len(a)):
     for j in range(i + k, len(a)):
          for x in range(j + k, len(a)):
               res = max(res, a[i] + a[j] + a[x])
print(res, end = ' ')

with open('27_B_10108.txt') as f:
     k = int(f.readline())
     n = int(f.readline())
     a = [int(x) for x in f.readlines()]
max1 = max2 = max3 = -10**20
for i in range(2*k, n):
     max1 = max(max1, a[i - 2*k])
     max2 = max(max2, a[i - k] + max1)
     max3 = max(max3, a[i] + max2)
print(max3)
