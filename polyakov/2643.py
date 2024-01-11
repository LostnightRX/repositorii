with open('2643.txt') as f:
     n, *a = map(int, f.readlines())
a.sort()
res = 0
l = 0
r = len(a) - 1
while l < r:
     if a[l] + a[r] > 100:
          r -= 1
     elif a[l] + a[r] < 100:
          l+= 1
     else:
          res += 1
          l+=1
          r-=1
print(res)
