from line import *
l()
# functionality of the try and except.
# Example-1
x,y=map(int,input("Enter two numbers:").split())
try:
    div=x/y
except ZeroDivisionError:
    print("A number can't divisible by zero.")
else:
    print("The division of entered two numbers are:",div)
l()
# Example-2
student_info={"Hardhik":38,"geeta":36,"leena":50}
print("The only students in the batch are:")
for i in student_info.keys():
    print(i)
key=input("Enter the key:")
try:
    value=student_info[key]
except KeyError:
    print("Sorry this student was not found in the group.")
else:
    print("The rule number of {} is:{}".format(key,value))
l()
# Example-3
print("Enter numbers:")
num_lst=[i for i in input().split()]
print(num_lst)
position=int(input("Enter the position you want:"))
try:
    result=num_lst[position]
except IndexError:
    print("Sorry,Your position is out of range.")
else:
    print("The element in the position is:",result)
l()

# we can also written the exception classes should be written in the form
# of tuple collection
import sys
try:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    z=x/y
except(IndexError,ValueError,ZeroDivisionError):
    print("sorry the code can't be exiguted.")
else:
    print("Result is:",z)
l() 

# not getting expected output
import sys

try:
    num1=int(sys.argv[1])
    num2=int(sys.argv[2])
    result=num1/num2

except Exception as ref:
        print("From except.")
        print("sorry unable to process....")
        print("reason:",ref)
else:
    print("The result is:",result)
l()

# we no need to know the error when we use this loggic
x,y=map(int,input("Enter two numbers with spaces:").split())
try:
    z=x/y
except Exception as ref:
    print("The reason is:",ref)
else:
    print("The result is:",z)
l()




