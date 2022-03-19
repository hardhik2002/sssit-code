#practicing nested for
n=int(input("enter number of lines:"))
c=int(input("enter number of colums:"))
for x in range(1,n+1):
    for y in range(1,c+1):
        print("Hardhik")
    print("")

print("________________________________")
#takimg name from the user
#and printing nuber also
cont=input("Enter your content:")
num=int(input("Enter your printing number:"))
for x in range(1,num+1):
   
    print(cont)    
    
print("________________________________")
out=1
while out<5:
    for i in range(1,6):
        print("*",end="")
    print("")
    out+=1
print("_________________________________")

for o in range(1,4):
    for i in range(1,6):
        print(i,end="")
    print("")
print("_________________________________")

#printing the piramid pattern
n=int(input("Enter number off lines dear:"))
for o in range(1,n+1):
    for i in range(1,o+1):
        print("*",end="")
    print("")
print("__________________________________")
#reversing the pyramid pattern.
n=int(input("Enter  number off lines dear:"))
for o in range(n,0,-1):
    for i in range(1,o+1):
        print("*",end="")
    print("")
for o in range(1,n+1):
    for i in range(1,o+1):
        print("*",end="")
    print("")#this code belongs to homework no.6
print("__________________________________")

#printing tables using nested for
table=int(input("Enter your table:"))
for o in range(1,table+1):
    for i in range(1,11):
        print(o,"X",i,"=",o*i)
    print("")
print("__________________________________")


























































































































