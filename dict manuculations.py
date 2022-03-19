#practicing dict manuculations.

#simple dict.
simple_dict={"Name":"Hardhik","Age":18,"Gender":"Male"}
print("The type is:",type(simple_dict))
print("The dict is:",simple_dict)
print("_"*80)
#converting list to dict.
"""sett=("Hardhik",18,"Haneesha",18,"Hampika",27)
print("Before applying the dict():",sett)
print("After applying the dict():",dict(sett))
print("_"*80)"""#this not possible.
simple_dict["Name"]="Haneesha"
print("After changing:",simple_dict)
print("_"*80)
#adding data to the eampty dict.
empty_dict={}
empty_dict["Name"]="Hampika"
empty_dict["Age"]=27
print(empty_dict)
print("_"*80)
#looping thye dict.
for dict in empty_dict:
    print(dict)
print("_"*80)#It shows only keys not the values.

print("Name is:",simple_dict["Name"])
print(simple_dict["Name"],"\'s age is ",empty_dict["Age"])
print("_"*80)
#Deleting an item.
capitals={"Telangana":"Hydrabad","Karnataka":"Benguluru","Maharastra":"Bombay"}
print("before deleting an item:",capitals)
del capitals["Telangana"]
print("After deleting an item:",capitals)
print("_"*80)

values=capitals.values()#same as keys()
print("Type is:",type(values))
print("Values are:",values)
print("_"*80)

#looping the dict using the for loop.
"""capitals={"Telangana":"Hydrabad","Andrapradesh":"Amaravathi"}
for item in capitals:
    key,value=item
    print(key,":",value)
print("_"*80)#getting error"""

#practicing update().
"""Adding a new item."""
name_age={}
key=input("Enter your name:")
value=input("Enter your age:")
name_age.update({key:int(value)})
print("The name and age are:",name_age)
print("_"*80)
"""Updating the existing key:value"""
name_roll={"Hardhik":45,"Haneesha":20091011}
name_roll.update({"Hardhik":int(105)})#It depends on value
print(name_roll)
print("_"*80)

D1={300:30,400:40}
D2={500:50,900:90}
D1.update(D2)#dict concatination.
print("Dict concatination:",D1)
print("_"*80)

#practicing setdefault(k,[d])

name_city={}
name,city=input("Enter your name:"),input("Enter your city:")
name_city.setdefault(name,city)#only for adding new item in dict collection.
print("name and city are:",name_city)
print("_"*80)

student={}
for num in range(1,5):
    students,roll=input("Enter your name:"),int(input("Enter your roll number:"))
    student.setdefault(students,roll)
print("The final dict is:",student)#It's completly working fine.
print("_"*80)

#fromkeys(iterable,value=None)
dict1={}
list1=["Hardhik","Haneesha","Hampika"]
dict1=dict1.fromkeys(list1,22)
print("The dict is:",dict1)
print("_"*80)

#using zip() It is not dict method.
#It is from collections module.

list1=["Hardhik","Haneesha","Hampika"]
list2=["Harathi","Linga reddy","Harish"]
z=zip(list1,list2)#It's getting error but the logic told by sheshi sir.
dict1=dict(z)
print("The dict is:",dict1)
print("_"*80)

#using get() method

d1={"Hardhik":18,"Haneesha":22}
print("GET():",d1.get("Haneesha",0))
print("_"*80)

#using pop() methode
#It will remove the item with given key and return.
#value of the key if key is existed.
print("Before popping the item:",d1)
print("The poped item is:",d1.pop("Hardhik"))
print("After popping the item:",d1)
print("_"*80)

#popitem() is similar to pop()
#popitem() writtens in tuple()
d2={22:200,33:300,44:400}
print("Before popitem():",d2)
print("Using popitem():",d2.popitem())
print("After popitem():",d2)
print("_"*80)






