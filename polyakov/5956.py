from functools import lru_cache


@lru_cache(None)
def simple(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def dels(n):
    g = []
    for i in range(2, int(n **0.5) + 1):
        if n % i == 0:
            if not simple(i):
                break
            g.append(i)
        if len(g) == 6:
            return True
    return False

def d(n):
    for i in range(2, int(n **0.5) + 1):
        if n % i == 0:
            return n//i
g = []
for i in range(2023, 10**9, 2023):
    if dels(i):
        g.append([i, d(i)])
for i in g[:5]:
    print(*i)
for i in g[-5:]:
    print(*i)
