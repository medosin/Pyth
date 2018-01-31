def three(num):
    outList=[]
    for i in range(num):
        inList=[]
        i+=1
        for x in range(i):
            x+=1
            inList.append(i*x)
        outList.append(inList)
    print(outList)
ss=int(input("enter the neumber"))
three(ss)                
