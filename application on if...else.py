#practicing nested if statement
age=int(input("Enter your age:"))
if age>=0:
    if age<5:
        print("Hi kid")
    elif age<13:
        print("Hi Teen")
    elif age<40:
        print("Hi adult")
    elif age<120:
        print("Hi old")
else:
    print("Are you a alien?")

print("_____________________________")
    
#having a if statement in a if statement is called
#nested if.
#__________________________________________________________

#example2
#it is based on minor and major and gender
#also included
gen=input("Enter your gender:")
age=int(input("Enter your age:"))

if gen in ["m","M"]:
    print("You are male")
    print("MAJOR") if age>=21 else print("MINOR")
elif gen in ["f","F"]:
    print("You are female")
    print("MAJOR") if age>=18 else print("MINOR")
    
print("_______________________________")





















































