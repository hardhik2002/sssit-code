name1=input("Enter your name:")
print("Hi",name1)
print("_____________________________")
age1=input("Enter your age:")
print("Your age is:",age1)
print("_____________________________")

#swapping of two numbers
x,y=10,20
x,y=y,x
print("this is 20:",x)
print("this is 10:",y)
print("_____________________________")
x,y=10,5
print("x % y--->",x%y)
print("x + y=",x+y)
print(x+y)
print("_____________________________")
# / vs // these both are different.
x,y=10,20
print("x/y:",x/y,type(x))
print("x//y:",x//y,type(y))
print("x*y-->",x*y)
print("x**y--->",x**y)
print("_____________________________")
#conditional operators.

x,y=10,20
print("x is small") if x<y else print("y is big")
print("______________________________")

#Membership operators.
"""It used for Iterable objects.
    It has two keywords
    -->In
    -->Not in

"""
ages=[18,21,17,32]
print("17 is in list:",17 in ages)
print("42 is in list:",42 in ages)
print("22 is in list:",18 not in ages)
print("______________________________")
string="Hardhik is a good boy."#trying out the string.
print("Does Hardhik is in string-->","Hardhik" in string)
print("Haneesha is not in string:","Haneesha" not in string)
print("_______________________________")

#trying out dict
dict={"Name:Hardhik","Age:18"}
print("trying out keyname:", "Name:Hardhik" in dict)
'''dict vadinappudu keyname and value renditini mention
cheyyali'''
print("_______________________________")
    
#Identity operators
x,y=20,40
print("X=20  Y=40")
print("Both are same") if id(x)==id(y) else print("Both are not same")
print("Both id's are same:",x is y)
print("Both id's are not same:",x is not y)
id1,id2=200,50734
if id(id1)==id(id2):
    print("Both are same")
else:
    print("No both are not same")

print("First id  and second id are not same-->",id1 is not id2)
print("_______________________________")
#Bitwise operators
x,y=10,29
print("x&y:",x&y)
print("x>>y:",x>>y)
#Actually ee topic medha inka konchum reaserch cheyyali.
print("_________________________________")
#input function
x=input("enter ur first number:")
y=input("enter ur second number:")
z=x+y
print("The sum of two numbers are:",z)
'''It does'nt work becuase sting gives only strings'''
print("________________________________")








































