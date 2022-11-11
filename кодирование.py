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
    return
def image():
    return
def information():
    return
