with open('26_7709.txt') as f:
     k = int(f.readline())
     n = int(f.readline())
     a = [[int(x) for x in i.split()] for i in f.readlines()]
p = [[0]*610 for _ in range(20)]
g = []
res = 0
for i in a:
     for x, j in enumerate(p):
          if not sum(j[i[0]:i[1] + 1]):
               res += 1
               for k in range(i[0], i[1] + 1):
                    p[x][k] = 1
               g.append(x + 1)
               break
print(res, g[-2])
