#practicing functions.
#example-->1
def l():#defining the function.
    print("_"*80)

x=[10,20,30]
print("sum of x is:",sum(x))
l()#calling the function.
y=(10,30,40)
print("max in y is is:",max(y))
l()
#this is user defined function.


#finding the sum of different numbers by using the functions.
def thesum(x,y,z):
    print("The sum is:",x+y+z)#x,y,z are formal parameters.
    l()
thesum(20,30,80)#these are actuall parameters.
thesum(200,400,500)
thesum(500,8000,501248)
#finding the square root.
n=int(input("Enter the number to get square root of it:"))
def square_root(x):
    s=x*x
    print("The sqare root of \'{}\' is:{}".format(n,s))

square_root(n)
l()
#finding factorial.
n=int(input("enter  the number to get facts:"))
def myfact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        return f

r=myfact(n)
print("the facts are:",r)
l()
#doing mathematical operations.
def my_math(x,y):
    sum,minus,multi=x+y,x-y,x*y
    print("sum is:{}\ndifference is:{}\nmultiplication is:{}".format(sum,minus,multi))
    
n=int(input("Enter your first value:"))
n2=int(input("Enter your second number:"))
my_math(n,n2)
l()

































