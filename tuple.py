# tup = (1,2,76,342,32,"green",True)
# # tup[0]= 30
# print(type(tup),tup)
# print(tup[0])
# print(len(tup))
# print(tup[-2])
# print(tup[6])
# print(tup.index(76,0,342))  #tuple.index(element, start, end)
# # print(tup[12])


# if 3421 in tup:
#     print("Yes 3421 present in this tuple")
# tup2 = tup[1:4]  #new tuple created
# print(tup2)

# country = ("Spain", "Italy", "India", "England", "Germany")
# if "Russia" in country:
#     print("Russia is present.")
# else:
#     print("Russia is absent.")

# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[3:7])     #using positive indexes
# print(animals[-7:-2])   #using negative indexes
# print(animals[1:8:3])

tup = (5,9,8,7,5,7,4,5,5,5,6,2,6,9,4,1,5,8) 
print(type(tup))
print(len(tup))
print(tup.index(7,0,18))

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)
print(type(countries))

