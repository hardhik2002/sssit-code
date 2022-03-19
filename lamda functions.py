def l():
    print("_"*85)
#adding two numbers using lamda.
my_add=lambda x,y:x+y
result=my_add(30,60)
print("The result is:",result)
l()
#finding the biggest number by usig normal function.
def biggest(x,y):
    if x>y:
        return x
    else:
        return y
print("Using a normal function.".center(150))
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
big_num=biggest(n1,n2)
print("The bigget number is:",big_num)
l()

#finding biggest number using lambda function.
print("Using a lambda function.".center(150))
biggest=lambda x,y:x if x>y else y
big_num=biggest(n1,n2)
print("The biggest number is:",big_num)
l()

#finding square_root list from a normal list.
lst=[1,2,3,4,5]
square=[]
def sq(x):
    s=x*x
    return s
for i in lst:
    root=sq(i)
    square.append(root)
print("The result is:",square)
l()
#now using map() function.
m=map(sq,lst)
list=list(m)
print("The result is:",list)

#using lambda in map().
print("By using lambda in map()".center(150))
list3=tuple(map(lambda x:x*x,lst))
print("Result is:",list3)
l()



#practicing filter().
"""Let's practice filter() after getting notes."""







































































