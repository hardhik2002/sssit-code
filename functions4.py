def l():
    print("_"*80)
"""sum of two numbers"""
#defining.
def sum(a,b):#formal parameters.
    sum=a+b
    print("The result is:",sum)
#calling
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
result=sum(n1,n2)#actual arguments
l()
"""returning the formal parameters"""
def multi(x):
    m=x*x*x
    return m#returning the local variables.
result=multi(10)#assigning function to a variable.
print("The result is:",result)
l()
"""finding the radius of the circle"""

def area_circle(radius):
    area=3.14*radius*radius
    return area
rad=int(input("Enter the radius of the circle:"))
result=area_circle(rad)
print("The area of the circle is:",result)
l()
#multiple return values.
def multi_return(x,y):
    a=x+y
    b=x-y
    c=x*y
    return a,b,c
n1=int(input("Enter the first value:"))
n2=int(input("Enter the second value:"))
addition,substraction,multiplication=multi_return(n1,n2)#if we assing this to single variable.
#It acts as tuple.
print("The addition is:{}\nThe substarction is:{}\nThe multiplication is:{}"
      .format(addition,substraction,multiplication))

l()




























