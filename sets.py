# s = {2,4,6,8}
# print(s)

# info = {"Carla",19,"Suraj",95,6}
# print(info)
# for sets in info:
#     print(sets)
    
    
# sets = set()
# print(type(sets))

# s1 = {1,2,5,6}
# s2 = {3,6,7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)
# print(s2.union(s1))
# s2.update(s1)
# print(s2,s1)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)
# cities.update(cities2)
# print(cities)
# cities3 = cities.intersection(cities2)
# print(cities3)
# cities.intersection_update(cities2)
# print(cities)
# cities4=cities.symmetric_difference(cities2)
# print(cities4)
# cities.symmetric_difference_update(cities2)
# print(cities)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)


