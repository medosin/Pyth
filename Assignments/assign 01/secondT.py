def two(myString,myKey):
    counter=0
    myLis=[]
    for a in myString:
        if a ==myKey:
            myLis.append(counter)
        counter+=1
    print(myLis)

two("my name is khan","a")            

