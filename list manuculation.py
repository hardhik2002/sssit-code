#Practicing list manuculation.
#sssit list manuculations.
lst1=["Hardhik","Haneesaha","Hampika"]
print("The list is:",lst1)
print("_"*50)
tuple1=("Hardhik","Haneesha","Hampika")
print("The tuple is:",tuple1)
print("Converting tuple to list:",list(tuple1))#This completely working fine.
print("_"*50)
r=range(11,21)
print(list(r))
print("_"*50)
#trying out for a string.
string="Hardhik."#here every charecter is changed to list.
print("String i schanged to list:",list(string))
print("_"*50)
#Indexing in the list.
lst=["Hardhik",18,"IARE","AI"]
print("The first one in list is:",lst[0])
print("_"*50)
lst=[11,12,13,14,15]#using while loop
index=0
while index<len(lst):
    print(lst[index])
    index+=1
print("_"*50)
for i in lst:#using for loop
    print(i)
print("_"*50)
#using append() method.
x=["Hardhik","Haneesha"]
x.append("Hampika")
print("The appended version is:",x)#This working fine.
print("_"*50)

lst=[]
item=input("Enter an item:")
lst.append(item)
print("The list is:",lst)#this working completely fine.
print("_"*50)
#using insert() method.
lst=[10,20,30]
lst.insert(2,33)
print("after inserting:",lst)
print("_"*50)#this working fine.
#second logic in insert().
lst=["Hardhik","Haneesha"]
lst.insert(1,"Hampika")
print("After insertion:",lst)
print("_"*50)#this is completly fine.
#third logic in insert().
lst=["Hardhik","Haneesha"]
lst.insert(1,"Hampika")
print("The inserted version is:",lst)
print("_"*50)
#practicing copy()
#copy() is different from reference copy
list1=[10,20,30,40,50]
print("Before uppliying copy():",list1 )
list2=list1.copy()
print("After applying a copy():",list2)
list2.insert(2,30)
print("After intersection:",list2)
print("The first list:",list1)#this is copy.
print("_"*50)

#applying if condition to the list.
gfamily=["Linga Reddy","Harathi","Hampika","Haneesha","Hardhik"]
input=input("Enter the required family member name:")
if input in gfamily:
    print(input," is in the list ",gfamily)
else:
    print("The  member is not belongs to gorla family.")
print("_"*50)
#using index() method
list1=[10,20,30,40,50]
pop=list1.index(20)
print("The found vesion is:",pop)#got expected output
#it gives the index number in the output.
print("_"*50)
#using count() method.
list1=[10,20,30,40,50,10,10,10,10]
count=list1.count(10)
print("The no.off 10 in the list1 is:",count)#this working fine.
print("_"*50)
#using pop() method
lst1=["Hardhik",18,(30+20j)]
print("Before using pop() method:",lst1)
list=lst1.pop()
print("After using pop() method:",list)
print("_"*50)
list1=[10,20,30,40,50]
print(list1.pop(1))#I'ts compeletly fine.
print("_"*50)
#using remove() method.
list1=[10,20,30,40,50]
print("Before using the remove() methode:",list1)
list1.remove(30)
print("after using remove() methode:",list1)#this working fine.
print("-"*50)
lst=["Hardhik","Hampika","Haneesha"]
print(lst.remove("Hardhik"))#In output we getting none
print("_"*50)
#using reverse() method.
list1=[10,20,30,40,50]
print("Before reversing the list:",list1)
list1.reverse()
print("After reversing the list:",list1)#we getting none in the output.
print("_"*50)




















































































