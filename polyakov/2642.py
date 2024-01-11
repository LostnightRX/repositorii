with open('2642.txt') as f:
     n, k, m, *a = map(int, f.read().strip().split())
a.sort()
print(a[-m],sum(a[:k:])//k)
