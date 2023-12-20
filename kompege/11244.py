with open('27_A_11244.txt') as f:
    k, n, *a = map(int, f.readlines())
res = 0
for i in range(len(a)):
    for j in range(i + k, len(a), k):
        res = max(res, a[i]*a[j])
print(res)

with open('27_B_11244.txt') as f:
    k, n, *a = map(int, f.readlines())
res = 0
g = []
for i in range(17):
    b = [a[x] for x in range(i, len(a), k)]
    g.append(b.pop(b.index(max(b))) * b.pop(b.index(max(b))))
    g.append(b.pop(b.index(min(b))) * b.pop(b.index(min(b))))
print(max(g))
