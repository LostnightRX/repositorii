with open('27-B.txt') as f:
    a=[int(x) for x in f]
    l=len(a)
    d=a+a
    allcost=[]
    res=0
    for i in range(l,(l//2)):
        cost=0
        v=d[i:i+l]
        for x in range(v):
            cost+=v[x]*x
        allcost.append(cost)
     mi=min(allcost)
            
