x = 4
#x is the variable of match
match x:
    #if n is 0
    case 0:
        print("x is Zero")
        #case with if condition
    case 4 if x % 2 == 0:
        print("x%2 = 0 and case is 4")
#Empty Case with if condition
    case _ if x<10:
        print("x is < 10")
#Default Case (Will only be matched if the above cases were not matched)
#so it is basically just an Else
    case _:
        print(x)
        
        
            