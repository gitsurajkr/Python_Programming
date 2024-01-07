# i = 0
# for i in range(6):
#     print(i)
#     if i ==4:
#         break
# else:
#     print("sorry no")

i = 0
while i<7:
    print(i)
    i = i+1
    if i ==4:
        break
else:
    print("sorry no")
    
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
    # break
else:
    print ("else block in loop")
print ("Out of loop")