def dels(n):
    counter = 3
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            counter += 2
    if counter == 117:
        return True
    return False

def d(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return n // i

for i in range(int(10**4.5)):
    i = i**2
    if (str(i)[:2] + str(i)[-2:]).count(str(i)[0]) == 4 and dels(i):
        print(i, d(i))
    
