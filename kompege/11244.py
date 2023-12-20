def A():
    with open('27_A_11244.txt') as f:
        k, n, *a = map(int, f.readlines())
    res = 0
    for i in range(len(a)):
        for j in range(i + k, len(a), k):
            res = max(res, a[i]*a[j])
    print(res)

def B():
    with open('27_B_11244.txt') as f:
        k, n, *a = map(int, f.readlines())
    res = 0
    for i in range(17):
        b = [a[x] for x in range(i, len(a), k)]
        res = max(b.pop(b.index(max(b))) * b.pop(b.index(max(b))), b.pop(b.index(min(b))) * b.pop(b.index(min(b))))
    print(res)

import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B, number=1))
