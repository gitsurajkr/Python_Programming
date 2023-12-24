# https://docs.python.org/3/library/time.html#time.strftime
import time
name = input("Enter Your name:").title()
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)

if (hour>=0 and hour<12):
    print("Good Morning",name)
elif (hour>=12 and hour<17):
    print("Good Afternoon",name)
elif (hour>=17 and hour<21):
    print("Good Evening",name)
else:
    print("Good Night",name)
