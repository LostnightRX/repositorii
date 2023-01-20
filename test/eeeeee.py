for i in range(1, 1999999999999):
    chislo=''
    num=(bin(i)[2:])
    if i % 2==0:
        chislo=num[:len(num) - 2:]+'101'

    if i % 2!=0:
        chislo = num[:len(num) - 2:]+'011'
    if int(chislo,2) > 200:
        print (i + 1)
        break

'''from turtle import *
left(90)
k = 15
forward(15*k)
right(90)
forward (15*k)
right(135)
forward (15*2**0.5*k)
pu ()

for x in range(15):
    for y in range(15):
        goto(x*k,y*k)
        dot(3)
done()

print (13+12+11+10+9+8+7+6+5+4+3+2+1)'''
