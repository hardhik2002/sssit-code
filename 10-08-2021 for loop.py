#practisin the for loop concept

lst=["Hardhik","Hampika","Haneesah"]
for i in range(1,11):
    print(i)
print("_______________________________")

name="Hardhik"
print("the given variable is:"+name)

for x in name:
    print(x)


print("_______________________________")

#trying out dictonory
dictnory={"Name":"Hardhik","age":18}
for x in dictnory:
    print(x)

print("_______________________________")
#printing tables
n=int(input("Enter your table number:"))
for i in range(1,11):
    print(n,"X",i,"=",n*i)
print("________________________________")

#finding the factors of the given value
n=int(input("Enter your value:"))
f=0
for i in range(1,n+1):
    if n%i==0:
        f=f+1
        print(i)
        
        
print("_______________________________")














