def calcArea(areaType):
    if areaType =="t":
        x=input("Enter num 1 \n ")
        y=input("Enter num 2 \n ")
        area=0.5*int(x)*int(y)
        print(area)
    elif areaType=="r":
        x=input("Enter num 1 \n ")
        y=input("Enter num 2 \n ")
        area=int(x)*int(y)
        print(area)    
    elif areaType=="s":
        x=input("Enter num 1 \n ")
        y=input("Enter num 2 \n ")
        area=int(x)*int(y)
        print(area)
    elif areaType =="c":
        x=input("Enter num 1 \n ")
        area=3.14*int(x)*int(x)
        print(area)
calcArea("c")             
