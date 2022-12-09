import random
a= list(input('ваше имя: '))
p = int(input('Укажите ваш пол(1 = женский, 2 = мужской): '))
Sogl=['Й','Ц','К','Н','Г','Ш','Щ','З','Х','Ф','В','П','Р','Л','Д','Ж','Ч','С','М','Т','Б','й','ц','к','н','г','ш','щ','з','х','ф','в','п','л','д','ж','ч','с','м','т','б']
gl = ['а','е','и','ё','у','ы','о','э','я','ю','Ё','Е','У','О','Ы','А','Э','Я','И', 'Ю']
ok = ['а','я']
ngl=[]
for i in range(len(a)):
    for b in range(len(gl)):
        if a[i]==gl[b]:
            ngl.append(a[i])
word=[]
b=''
for i in range(len(ngl)):
    word.append(random.choice(Sogl))
    word.append(ngl[i])
for i in range(len(word)):
    b+=word[i]
if p == 1:
    b+=random.choice(ok)
print(b)
