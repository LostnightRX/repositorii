s = '8'* 86
arg1 = '8888'
arg2 = '1111'
while(arg1 in s or arg2 in s):
    if s.count(arg2) > 0:
        s = s.replace(arg2, '8', 1)
    elif s.count(arg1) > 0:
        s = s.replace(arg1, '11', 1)
    else:
        continue
print(s)
