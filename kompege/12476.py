with open('24_12476.txt') as f:
     a = f.readline()
while 'ORO' in a or 'ROR' in a:
     a = a.replace('ORO', 'OR RO')
     a = a.replace('ROR', 'RO OR')
a = a.split()
m = 0
cc = 0
for i in a:
     if i.count('RO') >= 21:
          b = i.split('RO')
          for x in range(len(b) - 22):
               c = 'RO'.join(b[x:x+22])
               break
               cc = len(c)
               if c[:2] != 'RO':cc+=1
               if c[-1]!='O':cc+=1
               m = max(m, cc)
print(m)
