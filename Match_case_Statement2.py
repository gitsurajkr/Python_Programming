x =  int(input("Enter the value of x: "))
#x is the variable to match
match x:
    case 0:
        print("x is Zero")
        #case with if condition
    case 4:
        print("Case is 4")
    case _ if x != 90:
        print(x,"is not 90")
    case _ if x != 80:
        print(x,"is not 80")
    case _:
        print(x)
        
        