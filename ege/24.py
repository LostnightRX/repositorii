n = nmax = 0
with open('24.txt') as f:                                   #24.txt является текстовым файлом, он может меняться его просто надо держать в той же папке, что и прогу
    
    let = f.readline().replace('C', 'S').replace('D','S').replace('F','S')
let = let.replace('A', 'G').replace('O','G')
let = let.replace('SG', '*')
for i in let:
    if i == '*':
        n += 1
        nmax = max(n ,nmax)
    else:
        n = 0
print(nmax)
