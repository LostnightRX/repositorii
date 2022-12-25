import random
def foo():
    peremennaya = random.random()
    print(f'ваш рандом: {peremennaya}')
    while True:
        if input('кто первым прибыл в Америку? ') == 'викинги':
            print('ok')
            break
    for i in range(2):
        for j in range(2):
            print(i, j)
    if peremennaya != 0:
        flag = True
        print('вам повезло')
    else:
        flag = False
        print('изи фейл')
    x = random.triangular(2)
    y = random.triangular(23)
    z = random.triangular(10)
    if y <= x or not(z) == False:
        print("это ЛОЖЬ!")
    if y <= x or not(z):
        print('вернул правда')
    if peremennaya > 0.5:
        print('if1')
    elif peremennaya >= 0.2:
        print('elif2 true')
    else:
        print('в вашем случае все плохо')
    val = int(input())
    num=list(str((bin(val)[2:])))
    print(num.count('1'), num.index('0'))
    num.append(str(val))            
    num.sort(reverse=True)
    print(max(num), min(num))
    chislo='10' + str(num[2:]) + '0'

    s = []
    s.append(random.random())
    answer = s[len(s)-1]
    for i in range(100):
        s.append(i)
    data = list(map(int, input().split()))
    spisok= [x for x in data if int(x) - 12 <= answer - int(sum(answer))]

    divs.set(spisok)
    divs.add(int(input()))

    a = 12334567
    a = str(a)
    a = a.replace('12', 'aa')
    print(list(a))

    a = '1 2 3 4 5 6 7 8 9'
    b = a.split()

    res = b.sort(reverse = True)
    print(res)

    with open('17.txt') as f:       # загрузка с тектового файла в список с преобразованием в числа
       numbers=[int(x) for x in f]
       print(numbers[0])                  # обращение к первому элементу
       
    with open('24.txt') as f:       # загрузка с тектового файла одной строчки в список
       n=f.readline()
       prinT(n)


    with open('26.txt') as f:
        data=f.readlines()
        s,n=map(int,data[0].split())  # разбивка значений по двум переменным черем map (с чем делать, что делать)
        print(input('почуствуйте себя хакером, введите что-нибудь: '), s, n)
        
    with open('27_B.txt') as f:
        d=f.readlines()
        punkts=d[0]                 # получить первое значение, оно там в одно число на строку, в остальных случаях по два значения на строку
        for i in range (1,len(d)):      # c первого, потому что в первом одно общее число
            data.append(d[i].split())
            print(data)

    return
if __name__ == '__main__':
    print(foo())
