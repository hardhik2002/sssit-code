print("_"*50)
data=input("Enter your data:")
c=s=n=0
for i in data:
    if ord(i)>=64 and ord(i)<=90:
        c+=1
    elif ord(i)>=97 and ord(i)<=122:
        s+=1
    elif ord(i)>=48 and ord(i)<=57:
        n+=1
    else:
        print("Entered value is hipothetical")
print("No.off capitals:",c)
print("No.off small:",s)
print("No.off numbers:",n)
print("_"*50)

