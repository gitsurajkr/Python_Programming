# try:
#     l = [5,9,6,7,8,2]
#     i = int(input("Enter Number:"))
#     print(l[i])
# except:
#     print("Some Error Occured")
    
# # finally:
#     print("I am Always Excuted")


# def func1():
#  try:
#      l = [5,9,6,7,8,2]
#      i = int(input("Enter Number:"))
#      print(l[i])
#      return 1
#  except:
#      print("Some Error Occured")
#      return 0
     
#  finally:
#      print("I am Always Excuted")
     
# a = func1()
# print(a)

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")



    