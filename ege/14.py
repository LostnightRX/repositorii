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

