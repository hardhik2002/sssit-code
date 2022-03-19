#sum(iterable)-->it uses to sum the numbers.
my_marks=[27,55,66,88,44]
print("The total marks are:",sum(my_marks))
print("_"*80)
#it only applicable to the int values.
#not meant for string type.
#trying out the dict type.
my_dict={20:"Hardhik",50:"Haneesha"}
print("The total value of dict is:",sum(my_dict))
print("_"*80)
#trying out tupe type.
my_tuple=(20,30,40,609)
print("The sum in tuple is:",sum(my_tuple))
print("_"*80)

#min(iterable)->finding out the minimum value
#in the iterable.
lst=[10,20,30,40]
print("The list is:",lst)
print("The minimum value in the list is:",min(lst))
print("_"*80)
string_list=["Hardhik","Haneesha"]#It works on ASCII values.
print("Minimum value in the string list:",min(string_list))
print("_"*80)

#trying out the max(iterable)
lst=[20,30,13,200]
m=max(lst)
print("The list is:{}\nThe maximum value in the list:{}".format(lst,m))
print("_"*80)
#trying the max() for the string in list.
print("Max value in the string list:",max(string_list))
print("_"*80)

"""all(iterable)->bool | It will work same as logical and
     any(iterable)->bool | It will work same as logical or"""

lst=[10,0.1,"hardhik"]
print("all?",all(lst))
print("any?",any(lst))
print("_"*80)
t=(0,"Hardhik",None)
print("any:",any(t))
print("all:",all(t))
print("_"*80)



















