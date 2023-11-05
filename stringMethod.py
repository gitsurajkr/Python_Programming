#Upper()
str1 = "ABcgdHi"
print(str1.upper())

#lower()
str1 = "ABcgdHi"
print(str1.lower())

#strip()
str2 = "           Silver Spoon           "
print(str2.strip())

#rstrip()
str3 = "Hello!!!!!!!"
print(str3.rstrip("!!!"))

#replace()
str2 = "Silver Spoon"
print(str2.replace("Sp","M"))

#split()
str2 = "Silver Spoon"
print(str2.split("  ")) #split the string at the whitespace

#capitalize()

str1 = "Hello"
CapStr1 = str1.capitalize()
print(CapStr1)
str2 = "hello WoRlD"
CapStr2 = str2.capitalize()
print(CapStr2)

#center()
str1 = "Welcome to the Console"
print(str1.center(40))
str1 = "Welcome to the Console!!!!!"
print(str1.center(40,"_"))

#count()

str2  = "AbraCaDabra"
countstr = str2.count("a")
print(countstr)

#endswith()
str1="Welcome to the console!!!!!!!!!"
print(str1.endswith("!!!!"))

str1 = "Welcome To the Console!!!!!"
print(str1.endswith("to",4,10))

#find()
str1 = "His name is Dan.He is an honest man."
print(str1.find("Daniel"))
str1 = "Her name is Dan.He is an honest man."
print(str1.find("is"))

#Index()
str1 = "His name is Dan.Dan is an honest man."
print(str1.index("Dan"))
#str1 = "His name is Dan.Dan is an honest man."
#print(str1.index("Daniel"))

#isalnum()

str1 = "WelcomeToTheConsole"
print(str1.isalnum)

#isalpha()
str1 = "Welcome"
print(str1.isalpha())

#islower

str1 = "Hello World"
print(str1.islower())

#isprintable()
str1 = "We Wish You Merry Christmas"
print(str1.isprintable())

#isspace()

str1 = "     "#using spacebar
print(str1.isspace())
str2 = "       " #using spacebar
print(str2.isspace())

#istitle()

str1 = "World Health Organization"
print(str1.istitle())
str2 = "To Kill a Mocking Bird"
print(str2.istitle())

#isupper()
str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())

#startswith()
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

#swapase()

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

#title()
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())

