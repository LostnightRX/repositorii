with open('26_10107.txt') as f:
     n = f.readline()
     a = [list(map(int, x.split()[::-1])) for x in f.readlines()]
a.sort()
counter = 1
b = a[0]
for i in a[1:]:
     if i[1] >= b[0]:
          counter += 1
          if counter == 32: # это нужно, чтобы найти предпоследний процесс,
               break        # число 32 есть их количество по первому условию задачи, для нахождения этого количества нужно убрать этот if
          b = i
res = 0
for i in a[a.index(b):]:
     if i[1] > b[0]:
          res = max(res, i[1]- b[0])

print(counter, res)
