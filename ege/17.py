with open('17.txt') as f:
    d=[int(x) for x in f]
    x=[i for i in d if i%17==0]
    minX=min(x)
    count=0
    sums=[]
    for i in range(1,len(d)):
        if d[i]%minX==0 or d[i-1]%minX==0:
            count+=1
            sums.append(d[i]+d[i-1])       
    print(count,max(sums))
