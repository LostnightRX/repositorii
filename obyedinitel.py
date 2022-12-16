def systems():
    N10 = int(input('введите число '))
    p = int(input("введите сс "))
    Np = 0
    k = 1
    while N10 != 0:
        Np = Np + (N10 % p) * k
        k = k * 10
        N10 = N10 // p
    print(Np)
def numSys():
    p = int(input())
    Np = int(input())
    k = int(1)
    N10 = int(0)
    while p != 0:
        N10 = N10 + (Np % 10) * k
        k = k * p
        Np = Np // 10
        p = p - 1
    print("N10= ", N10)
    return

def operation():#Сообщение от Сола Гудмана#
    print("введите p (2 < p <= 10): ")
    p = int(input())
    for X in range(1, p - 1):
        for Y in range(1, p - 1):
            Z = (X * X / p) * 10 + (X * Y % p)
            print(f'{Z:03}')
        print("\n")
        return
    return
def distance(x,y):
    k=7
    for i in range(7):
        if x%10==y%10:
            k=k-1
        x=x//10
        y=y//10
    return k
def hemming(): 
    a='0123456789'
    nums=list(a)
    print(nums)
        
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    b='0000000 000111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    hem = b.split()
    print(hem)
    for i in range(len(hem)):
        hem[i]=int(hem[i])
    print(hem)        
    
    cod=int(input("код="))

    min=distance(cod,hem[0])
    imin=0
    for i in range(10):
        D=distance(cod,hem[i])
        if D:
            min=D
            imin=i
    if min==0:
        print(f"Код верный: символ {nums[imin]}")
    elif min==1:
        print(f"Код исправлен: символ {nums[imin]}")
    else:
        print(f"Код неверный")
def ():
        abc=['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','а','б','в','г','д','е','ж','з','и','й','к']
    ab=['._','-…','.--','--.','-..','.','…-','--..','..','.---','-.-','._','-…','.--','--.','-..','.','…-','--..','..','.---','-.-']
    word1=list(input())
    word2=[]
    for i in range(len(word1)):
        word2.append(ab[abc.index(word1[i])])
    B=''.join(word2)
    print(B)
