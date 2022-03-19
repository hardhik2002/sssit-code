from line import *
l()
# Example-1
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible for vote....") 
else:
    try:
        raise ZeroDivisionError()
    except ZeroDivisionError:
        print("You are not elligile for vote")


