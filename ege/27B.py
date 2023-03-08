with open('27-B.txt') as f:
        s=[int(x) for x in f]
        s.pop(0)
    l=len(s)
    sp=[]
    s=s+s
    start=0
    finish=l #длина списка
    step=50000
    mini_old=0
    while True:
        sp=[]
        for i in range(start,finish,step):
            d=s[i:i+l]
            cost=0
            for x in range(l):
                ind=x
                if x>=l//2: ind=l-x
                cost+=d[x]*ind
            sp.append(cost)
            print(i, cost)

        index=sp.index(min(sp))
        mini=start+index*step

        print("точка минимума в диапазоне и стоимость", mini, min(sp))
        if mini_old==mini and step==1:
            print("Искомый ответ-", mini+1)
            exit()

        mini_old=mini
        start=mini-step
        finish=mini+step
        step//=10
        if step==0:step=1

        print(start,finish,step)

