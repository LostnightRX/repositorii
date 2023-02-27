with open('27-A.txt') as f:
    a = [int(x) for x in f]
    n = a.pop(0)
    g = []
    l = len(a)
    a = a + a
    for j in range(l):
        c  = a[j : j + l]
        cost = 0
        for i in range(len(c)):
            if i >= len(c) //2:
                ind = len(c)- i
                cost  += ind * c[i]
            else:
                cost += i * c[i]
        g.append(cost)
    print(g.index(min(g)) + 1)
