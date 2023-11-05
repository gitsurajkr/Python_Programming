#Explict Typecasting
string = "15"
number = 7
string_number = int (string) #it will throw error if the string is not a valid integer
sum = number + string_number
print("The sum of both number is: ",sum)

#Implict Typecasting
'''Python automatically converts a to int '''
a = 7
print (type(a))

'''Python automatically converts b to float'''
b = 3.0
print(type(b))

'''Python automatically converts c to float as it is a float addition'''
c = a+b
print(c)
print(type(c))

a = "1"
#a = 1
b = "2"
#b = 2
print (int(a)+int(b))
c = 1.9
d = 8
print(c+d)