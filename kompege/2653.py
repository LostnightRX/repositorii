from tqdm import tqdm
with open('26_2653.txt') as f:
     n, *a = map(int, f.read().strip().split())
k = sum(a)
c = set(range(1, k + 1))
r = set()
for i in tqdm(a):
     b = set()
     for j in r:
          b.add(j+i)
     b.add(i)
     r |= b
res = list(c - r)
res.sort()
print(len(res), res[-1])
