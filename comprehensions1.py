def l():
    print("_"*80)
def normal():
    print("This is in normal way.".center(150))
    l()
def comp():
    print("This is in comprihension way.".center(150) )
    l()
#practicing comprehensions.
#It is the shortest way to write a code.
#we can build a consised code by using
#comprehensions.
"""
example-1

"""
normal()
empty_list=[]
for i in range(1,11):
    empty_list.append(i)
print("The list is:",empty_list)
l()
comp()

list=[i for i in range(1,11)]
print("The list is:",list)
l()

#example-2
square_list=[square*square for square in range(1,11)]
print("The square list is:\n",square_list)
l()
#trying same with input values.
n=int(input("Enter the number you want:"))
square_list=[i*i for i in range(1,n+1)]
print("The square list is:\n",square_list)
l()

#doing the same thing in if conditions.
print("Printing even number list".center(150))
l()
lst=[i for i in range(1,21) if i%2==0]
print("The list is:",lst)
l()
#moving to strings.
name_list=["Hardhik","Sharukh","sai","venkat"]
c_list=[i for i in name_list if i[0]=="S" or i[0]=="s" ]
print("The names that starts with s are:\n",c_list)
l()

#using methods.
c_list=[i for i in name_list if i.startswith("s") or i.startswith("S")]
print("The names that starts with s are:",c_list)
l()
#printing names which starts with only upper case.
c_list=[i for i in name_list if i.upper()]#not getting expected output.
print("Names that starts with capital letter:",c_list)
l()
#trying out the input() function.
print("Enter 3 numbers with spaces:")
list=[int(i) for i in input().split()]
s=sum(list)
l()
print("result is:",s)
print("Enter your name twice:")
list=[i for i in input().split()]#['Hardhik']
list2=[i for i in input()]#['h', 'a', 'r', 'd', 'h', 'i', 'k']
print("Your name without using split:",list2)
print("Your name with using split:",list)
l()












































