with open('2639.txt') as f:
     n, k, *a = map(int, f.read().strip().split())
a.sort()
print(a[k:-k:][-1], sum(a[k:-k:])//(n-2*k))
