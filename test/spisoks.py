import random
def sort(isreverse):
    a = [int(random.random() * 100) for _ in range(int(input('количество элементов списка: ')))]
    for j in range(len(a)):
        maxa = 0
        for i in range(len(a) - j):
            if a[i] > maxa:
                maxa = a[i]
        a.append(a.pop(a.index(maxa)))
        #print(a)                                   это можно использовать для отслеживания изменения списка
    if isreverse:
        a = a[::1]
    else:
        a = a[::-1]
    return a
def binary():
    a = [25, 6, 4, 18, 32, 64, 124]
    print(a)
    while len(a) != 1:
        if a[len(a) // 2] > a[len(a) // 2 - 1]:
            a = a[:len(a) // 2:]
        else:
            a = a[len(a) // 2::]
    print(a[0])
if __name__ == '__main__':
    i = int(input('1 - сортировка рандомного списка\n 2 - бинарный поиск'))
    if i == 1:
        print(sort(True))
    elif i == 2:
        binary()
        
