from line import *
#files read mode
f=open("txt-file-3.txt","r")#default is read mode
r=f.read(100)
print("The data is:\n",r)#this is working well.
l()
position=f.tell()#to find where is the file pointer.
print("The file pointer is in:",position)#the file pointer is in 102
l()
s=f.seek(2)#to take the file pointer to our wish position.
print("The file pointer went to:",s)
p=f.tell()
print("the file pointer after using seek():",p)
l()
#practicing readline()->str function.
l1=f.readline()
l2=f.readline()
print(l1,l2)
l()
#readlines()->lst it read all lines in the file but in list form.
lines=f.readlines()
print("the entire lines are:\n",lines)
l()

f.close()






























