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