with open('27-A_12257.txt') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
k = 113
res = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        if sum(a[i:j]) % k == 0:
            res = max(res, len(a[i:j]))
print(res)

with open('27-B_12257.txt') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
k = 113
c = [0]*(len(a) + 1)
for i in range(1, len(c)):
    c[i] = a[i-1] + c[i-1]
b = list(map(lambda x: x % k, c[:]))
g = []
for i in range(k):
    g.append(len(b) - b[::-1].index(i) - b.index(i) - 1)
print(max(g))
    
