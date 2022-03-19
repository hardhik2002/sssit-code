#defining a line
def l():
    print("_"*80)
line=l





"""assigning function object to a variable.Then that variable is also
acts as function."""
def greet():
    print("Hello")
print("Before assigning to a variable.",greet)
    
x=greet

print("After assigning to variable:")
x()
line()

"""Passing a function object as an argument to another function"""


"""def mom():
    a=print("MOM")
    return a
def father(func):
    x=func()
    y=x+"my dear"
    return y
r=mom()
print("Result is:",r)
father(mom)"""#I have lots of doubts in this code.


'''Defining a function inside another function.
'''

def my_logic():
    def star_logic():
        for i in range(1,11):
            print("*",end="")
    star_logic()
    print("\n Hi \n")
    star_logic()
print("The entire logic is:\n")
my_logic()
print("\n")
line()
























