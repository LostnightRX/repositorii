with open('27_A_9848.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
res = 0
for i in range(len(a)):
    for j in range(i + k + 1, len(a)):
        res = max(res, sum(a[i:j]))
print(res)

res = float('-inf')
with open('27_B_9848.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
b = [0]*len(a)
for j, i in enumerate(a):
    b[j] += i + b[j-1]

for i in range(k + 1, len(b)):
    res = max(res, b[i] - b[i-k - 1])
print(res)
