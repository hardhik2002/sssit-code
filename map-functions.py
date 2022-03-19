def l():
    print("_"*80)
#using map() function.
"""
syn:map(func,*iterables)->map object.
"""
#example-1
lst=[1,2,3,4,5]
def sq(x):
    s=x*x
    return s
m=map(sq,lst)
lst_sq=list(m)
print("List after using map:",lst_sq)
l()
list1=[1,2,3,4,5]
def square_root(x):
    square__root=x*x
    return square__root
m=map(square_root,list1)
lst_sq=list(m)
print("Type is:",type(m))
print("Actual list is:",list1)
print("Result after using list:",lst_sq)
l()
#using lambda function in the place of regular function.


lst=[1,2,3,4,5,6,7]
m=list(map(lambda x:x*x*x,lst))
print("Cube root list is:\n",m)
l()
#trying same logic in consised.
print("Result is:",list(map(lambda x:x*x,[1,2,3,4,5])))
l()



























































