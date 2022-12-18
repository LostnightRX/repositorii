import math
from turtle import*
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for i in range(11):
    for j in range(11):
        goto(i * 30, j * 30)
        dot(5)
done()
