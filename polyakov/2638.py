with open('2638.txt') as f:
     n, k, *a = map(int, f.read().strip().split())
a.sort()
res = 0
b = a[-k:]
for i in b:
     res += i*0.2
print(a[-k-1], int(res))
