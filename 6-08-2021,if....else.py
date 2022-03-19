#Trying out the if....else
#example1

'''allow only if user age is 18+ into the site'''
age=int(input("Enter your age:"))
print("_______________________________")
print("You are eligible for this site") if age>18 else print("You are not eligible for this site")

#trying out if..else by using Iterables
print("_______________________________")
name=input("Enter your name:")
name_lst=["Hardhik","Haneesha","Hampika"]
if name in name_lst:
    print("Welcome, you are a family member")
else:
    print("Sorry, you are not a family member")

print("________________________________")
#Trying out with strings
gender=input("Enter your gender:")
if gender in "Mm":
    print("Your gender is male.")

if gender in "Ff":
    print("You are a Female.")

else:
    print("May be you are gay.")
    


print("_________________________________")
print("_________________________________")































