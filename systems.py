N10 = int(input('введите число '))
p = int(input("введите сс "))
Np = 0
k = 1
while N10 != 0:
    Np = Np + (N10 % p) * k
    k = k * 10
    N10 = N10 // p
print(Np)
