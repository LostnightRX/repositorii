with open('27_A_9755.txt') as f:
     k = int(f.readline())
     n = int(f.readline())
     a = [int(x) for x in f.readlines()]
res = 10**10
for i in range(len(a)):
     for j in range(i + k, len(a)):
          for x in range(j + k,len(a)):
               res = min(res, a[i] + a[j] + a[x])
print(res)

with open('27_B_9755.txt') as f:
     k = int(f.readline())
     n = int(f.readline())
     a = [int(x) for x in f.readlines()]
s1 = s2= s3 = 10**20
for i in range(2*k, len(a)):
     s1 = min(s1, a[i-2*k])
     s2 = min(s2, s1 + a[i-k])
     s3 = min(s3, s2 + a[i])
print(s3)
