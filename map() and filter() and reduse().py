from line import *
from functools import *
#practicing map()
"""
syn:map(func,*iterables)->map object.
"""
#Example-1
print("Doing square by using map() function.")
l2()
num_list=[1,2,3,4,6]
print("The original list is:",num_list)
def square(x):
    s=x*x
    return s
m=list(map(square,num_list))
print("The result is:",m)
l()
print("Doing sum in list numbers by using map function.")
l2()
num_list=[22,44,99,55,88,33,88,99,33,22]
def sume(x):
    sum_num=sum(num_list)
    return sum_num
m=list(map(sume,num_list))
print("The sum list is:",m)
l()
#doing same as example-1 but
#by using lambda functon.
num_list=[1,2,3,4,5,6]
m=list(map(lambda x:x*x,num_list))
print("The square list is:",m)
l()
num_list=[12,32,43,64,55]
m=list(map(lambda x:x+x,num_list))
print("The sum list is:",m)
l()
#Example-3
print("Finding the area of the circle")
l2()
radius_list=[1.1,2.2,3.3,4]
m=list(map(lambda x:3.14*x*x,radius_list))
print("Area list is:",m)
l()
def area_of_circle(rad):
    area=3.14*rad*rad
    return area
m=list(map(area_of_circle,radius_list))
print("Area list is:",m)
l()
"""
Practicing reduce function
"""
#To use reduce() we should import functools
#module.
#Example-1
num_list=[1,2,3,4,5,6]
f=reduce(lambda x,y:x*y,num_list)
print("Fact is:",f)
l()
"""
Practicing filter().
"""
#Example-1
str_list=["anu","sai","roja","srija","kooja","sri"]
f=list(filter(lambda x:len(x)==3,str_list))
print("The names that only with three letters are:",f)
l()









