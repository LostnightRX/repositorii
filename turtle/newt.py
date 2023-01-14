from turtle import*
forward(15 * 30)
goto(0, -15 * 30)
left(90)
forward(15 * 30)
pu()
for i in range(20):
     for j in range(20):
          goto(i * 30, j * 30 - (15*30))
          dot(5)
