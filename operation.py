#Сообщение от Сола Гудмана#
print("введите p (2 < p <= 10): ")
p = int(input())
for X in range(1, p - 1):
    for Y in range(1, p - 1):
        Z = (X * X / p) * 10 + (X * Y % p)
        print(f'{Z:03}')
    print("\n")
