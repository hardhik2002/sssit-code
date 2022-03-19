def l():
  print("_"*80)
"""We can assign a function to a variable"""
def assign_function():
    print("Hi")
    
print("type is:",type(assign_function))
print("hcode is:",assign_function)#we get hash code
assign_function()#calling function
l()
#assigning a funtion to a variable
x=assign_function
print("hcode:",x)#we get hcode
x()#calling function after assigning to the variable.
l()
"""We can pass a function as an argument
to another
"""
def func1():#defining a function
  a="Hi"
  return a

def func2(func):#secong function func is an argument
  b=func()
  c=d+"My dear"
  return c

d=func1()
print("result of func1:",d)

e=func2(func1)#passing func1 function as an argument.
print("Result of func2:",e)
l()

"""          We can define a function inside a function
"""

def original_function():
  def stars():
    for i in range(1,11):
      print("*",end="")
  stars()
  print("\nHi I am Hardhik")
  stars()
  print("\nHardhik Reddy")
  stars()


print("The stars and hardhik are here")
original_function()
print("\n")
l()

"""
                        A function return another function

"""


#If you wnat to use the result of inner function inside of
#outerfunction then inner function need to be return value.
#case-1
def outer_function():
  def inner_function():
    x=100
    return x
  value=inner_function()
  print("The value is:",value)

#calling outer function.

outer_function()
l()

#case-2

def outer_function():
  def inner_function():
      bd="Hi,I am Hardhik."
      return bd
  intro=inner_function()
  return intro
#calling
result=outer_function()
print("Hardhik introduse yourself:\n",result)
l()

#case-3

"""If you want use the inner function
outside of outerfunction theb outer function
need to return inner function."""

def outer_function():
  def inner_function():
    a=10
    return a
  return inner_function
outer=outer_function()#hcode of inner_function 
result=outer()
print("Result is:",result)
l()

#example on non-local keyword.
def outerfunc():
  x=30
  def innerfunc():#I didn't understand this code.
    nonlocal x
    print("Innerfunc x:",x)
  innerfunc()


outerfunc()

















































