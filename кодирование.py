import math

def solve():
    print("кодирование: 1 - инфы, 2 - звука, 3 - изображения")
    n = int(input())
    if n == 1:
        res = information()
    elif n == 2:
        res = sound()
    elif n == 3:
        res = image()
    else:
        print("это не то, ты не достоин совершщеннства решения этой задачи!!!!!")
        return
    print(res)
    return

if __name__ == '__main__':
    solve()


def sound():
    print("что неизвестно? (1 - объем, 2 - частота дискретизации, 3 - время записи, 4 - разрядность квантования")
    arg = int(input())
    if arg == 1:
        print("введите частоту, время, разрядность последовательно через пробел")
        H, t, b = map(int, input().split())
        return H * t *b
    elif arg == 2:
        print("введите объем, время, разрядность последовательно через пробел")
        I, t, b = map(int, input().split())
        return I // (t * b)
    elif arg == 3:
        print("введите объем, частоту, разрядность последовательно через пробел")
        I, H, b = map(int, input().split())
        return I // (H * b)
    elif arg == 4:
        print("введите объем, время, частоту последовательно через пробел")
        I, t, H = map(int, input().split())
        return I // (H * t)
    else:
        return "неверные входные данные"

def image():
    print ("что неизвестно? (1 - количество цветов, 2 - глубина избражения)")
    arg = int(input())
    if arg == 1:
        print("введите глубину изображения")
        i = int(input())
        return 2 ** i
    elif arg == 2:
        print("введите количество цветов")
        N = int(input())
        return math.log(N, 2)
    else:
        return "неверные входные данные"
def information():
    print("что нужно найти? (1 - информационный объем текста, 2 - мощность алфавита, 3 - количество символов, 4 - информационный вес символа)")
    arg = int(input())
    if arg == 1:
        print("известен ли информационный вес символа? (1 - да, 0 - нет)")
        tr = bool(input())
        if tr:
            print("введите инф вес символа, количество символов последовательно через пробел")
            i, K = map(int, input().split())
            return i * K
        else:
            print("введите мощность алфавита, количество символов последовательно через пробел")
            N, K = map(int, input().split())
            return math.log2(N) * K
    return

def construct(a, arg):
    #аргумент это та величина, из которой переводим
    # 1 - байт, 2 - Кб, 3 - Мб, 4 - Гб
    if arg == 1:
        return a * 2 ** 3
    elif arg == 2:
        return a * 2 ** 13
    elif arg == 3:
        return a * 2 ** 23
    elif arg == 4:
        return a * 2 ** 33
    else:
        return
    
