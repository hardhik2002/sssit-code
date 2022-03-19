def l():
    print("_"*80)


#practicing distructors.

'''
example-1

'''
class sample:
    def __init__(self):
        print("Const is invoked")
        self.x=10#instance
    def getdata(self):
        print("x value is:",self.x)


#calling
s1=sample()
s1.getdata()
s1=None
'''s1.getdata()'''#attribute error.
print("Object2...")
s2=sample()
s2.getdata()
s2=None
l()

'''
example-3
'''
import sys
class sample:
    def __init__(self):
        print("const is invoked...")
    def __del__(self):
        print("Dest is invooked...")
#calling
s1=sample()
s2=s1#rederence copy
s3=s2
print("Ref.count is:",sys.getrefcount(s1))
s1=None
s2=None
s3=None
l()




































































