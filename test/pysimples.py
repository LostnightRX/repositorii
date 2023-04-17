import PySimpleGUI as sg

sg.theme('LightBlue2')  # Set the theme

s=['1','2','3','4','5','6','7','8','9','10','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27a','27b']
a=[
#1
'''
1) найти точки, через который проходят пути между пунктами
2) найти все возможные варианты путей и посчитать их сумму
3) сложить ответы
''',
#2
'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not(y <= x) or (z <= w) or not z)
                print([x, y, w, z] if not f else '')
''',
#3
'''
1) применить фильтры по нужным значкениям
2) посчитать и умножить(при необходимости) на нужное количество
''',
#4
'''
важно помнить про прямое условие фано - код одного символа не может быть началом кода другого символа

1) посмотреть, сколько раз встречается каждая буква
2) на основе данных условия задать для буквы, повторяющейся наибольшее количество раз, код c минимальным количеством знаков
3) далее по бинарному дереву выстроить значения для других букв
''',
#5
    '''#    for n in range(1,100):      решение из демо 2023
#        s = bin(n)[2:]
#        if s.count('1') % 2 == 0:
#            s = '10' + s[2:] + '0'
#        else:
#            s = '11' + s[2:] + '1'
#        if int(s,2) > 40:
#            print(n)
#            break

    for n in range(1, 100000):          #решение досрочного 2022
        val = f'{n}'
        if n % 2 == 0:
            val += '10'
        else:
            val = '1' + val + '01'
        if int(val, 2) > 516:
            print(n)
            break''',
#6
'''
from turtle import*
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for i in range(11):
    for j in range(11):
        goto(i * 30, j * 30)
        dot(5)
done()
''',
#7
'''
1) вспомнить формулу для вычисления нужной величины
2) написать формулы для случаев "до" и "после"
3) определить изменение данной величины и получить то, что требуется
''',
#8
'''
from itertools import product

k=0
n='16 36 56 76 61 63 65 67'
nn=n.split()
nums=product('01234567',repeat=5)
for n in nums:
    numb=''.join(n)
    if numb.count('6')==1 and numb[0]!='0':
        if all(not(x in numb) for x in nn):
            k+=1
print(k)
''',
#9
'''
=СЧЁТЕСЛИ($A1:$F1; A1)
=СУММ(G1:L1)
= ЕСЛИ(M1 = 8;1;0)
=ЕСЛИ(И(H1=2; $N1 = 1); B1; 0)
=(СУММ(A1:F1) - СУММ(O1:T1))/4
=ЕСЛИ(U1 <= СУММ(O1:T1);1;0)
=СУММ(V1:V10000)
''',
#10
'''
1) Ctrl + F в параметрах ставим галочки "учитывать регистр" + "только слово целиком"
2) количество результатов будет показываться
''',
#12
'''
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
''',
#13
'''
1) маркируем старт единицей
2) анализировать пути по одной дороге(вохможно несколько случаев)
3) сложить суммы путей
''',
#14
'''
N10 =  (3* 16**2018 - 2 * 8**1028 - 3 * 4**1100 - 2**1050 - 2022)
p = 4
Np = 0
k = 1
while N10 != 0:
    Np = Np + (N10 % p) * k
    k = k * 10
    N10 = N10 // p
print(Np)
print(str(Np).count('3'))
''',
#15
'''
for a in range(0,100):
    if all(((x%3==0) <= (x%5!=0)) or ((x+a)>=70) for x in range(1,10000)):
        print(a)
''',
#16
'''
from sys import setrecursionlimit
setrecursionlimit(2030)
def f(x):
    if x==1:
        return 1
    if x>1:
        return x*f(x-1)
print(f(2023)/f(2020))
''',
#17
'''
with open('17.txt') as f:
    d=[int(x) for x in f]
    x=[i for i in d if i%17==0]
    minX=min(x)
    count=0
    sums=[]
    for i in range(1,len(d)):
        if d[i]%minX==0 or d[i-1]%minX==0:
            count+=1
            sums.append(d[i]+d[i-1])       
    print(count,max(sums))
''',
#18
'''
1) левый верхний угол бурём значение из 1 таблицы
2) в ячейке справа складываем значение этой ячейки из таблицы 1 и значения 1 ячейки, аналогично для ячейки снизу
3) далее используем макс()+зн этой ячейки из таблицы 1 (макс() для ячеек сверху с снизу относительно даной)
4) за барьерами используем формулы сложения верхнего и данного значения , аналогично для горизонтального.
''',
#19
'''
1) найти точку входа(цель данной игры)
2) определить возможные действия(ходы)
3) разыграть сценарий, при котором выполняются условия задачи и найти интересующее значение
''',
#20
'''
1) найти точку входа(№1 в #19)
2) разыграть все сценарии при которых выполняются условия задачи
''',
#21
'''
1) выполнить 2 первых пункта #19
2) разыграть все возможные сценарии, при которых выполняются условия задачи(в данном случае нужно записать минимальное значение)
''',
#22
'''
просто отрисовать по секундам а затем посчитать максимальное значение
''',
#23
'''
def f(x,y):
    if x > y or x == 17: return 0
    elif x == y: return 1
    return f(x + 1, y) + f(x * 2, y)
print(f(1, 10) * f(10, 35))
''',
#24
'''
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
''',
#25
'''
for i in range(2023, 10**10, 2023):
    num = str(i)
    if num[0] == '1' and num[2:6] == '2139' and num[-1] == '4':
        print(i, i//2023)
''',
#26
'''
with open('26.txt') as f:
    s = [int(x) for x in f]
    s = sorted(s[1:], reverse = True)
    n, mini = 1, s[0]
    for i in range(1, len(s)):
        if s[i] + 3 <= mini:
            mini = s[i]
            n += 1
    print(n , mini)
''',
#27a dosrok
'''
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
''',
#27b dosrok
'''
with open('27-B.txt') as f:
        s=[int(x) for x in f]
        s.pop(0)
    l=len(s)
    sp=[]
    s=s+s
    start=0
    finish=l #длина списка
    step=50000
    mini_old=0
    while True:
        sp=[]
        for i in range(start,finish,step):
            d=s[i:i+l]
            cost=0
            for x in range(l):
                ind=x
                if x>=l//2: ind=l-x
                cost+=d[x]*ind
            sp.append(cost)
            print(i, cost)

        index=sp.index(min(sp))
        mini=start+index*step

        print("точка минимума в диапазоне и стоимость", mini, min(sp))
        if mini_old==mini and step==1:
            print("Искомый ответ-", mini+1)
            exit()

        mini_old=mini
        start=mini-step
        finish=mini+step
        step//=10
        if step==0:step=1

        print(start,finish,step)

''',
]
# Define the layout
layout = [[sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(40,10), key='outputt')],
          [sg.Button('вывод', font=('Consolas', 12), button_color=('white', '#4CAF50'), key='process'),
           sg.Button('сбежать', font=('Consolas', 12), button_color=('white', '#4CAF50'), key='exit'),
           sg.Button('url', font = ('Consolas',12), button_color=('white', '#4CAF50'), key = 'url')]]

# Create the window
window = sg.Window('саратов by Степанов Михаил v1.0', layout)

# Event loop
while True:
    event, values = window.read()

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        choice=a[s.index(values['Combo'])]
        #print(choice)
        #window['outputt'].update('')
        window['outputt'].update(choice)
    elif event == 'url':
        layout2 = [[sg.Text('прикол')], [sg.Button('cancel', font = ('Сonsolas', 12), button_color = ('white', '#4CAF50'))]]
        window2 = sg.Window('это ссылки', layout2, )
        while True:
            event2 = window2.read()
            if event2 == 'cancel' or event2 == sg.WINDOW_CLOSED:
                window2.close()
                break
    elif event == 'exit':
        break

# Close the window
window.close()
