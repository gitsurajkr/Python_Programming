#The continue statement skips the rest of the loop statements of the loop statements and cause the next
#iteration to occur

# for i in [2,34,5,6,8,0]:
#     if (i % 2 != 0):
#         continue
#     print(i)
        
for i in range (12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 x",i, "=",5*i)