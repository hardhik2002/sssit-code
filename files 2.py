from line import *
f=open("txt-file-2.txt","w")
print("enter your own data".center(150))
print("press ^ to exit.".center(150))
l()
txt=input()
while txt!="^":
    f.write(txt+"\n")
    txt=input()

f.close()
print("Your file is saved.")

