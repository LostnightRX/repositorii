import math
ans = [2]
for i in range(1001):
    for j in range(2, i):
        if i % j == 0:
            if ans.count(i) > 0:
                ans.remove(i)   
            break
        if ans.count(i) == 0:
            ans.append(i)
for n in range(1000):
    if ans.count(105 + 6*n) != 0:
        print(n)
        break
