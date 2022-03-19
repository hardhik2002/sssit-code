#defining a line.
def l():
    print("_"*80)
"""
Has-A relationship.

"""
#has a relationship first basic example.
class super:
    def method1(self):
        print("This is method1 of super class.")
class sub:
    def method2(self):
        #calling method1 of super class inside of the sub class
        s=super()
        s.method1()#HAS-A relationship.
        
        print("This is the method2 of the sub class.")


su=sub()
su.method2()
l()


'''
trying out this with instance method.
'''
class super:
    @classmethod
    def method1(cls):
        print("cls method-1 of super class.")
        l()
class sub:
    def method2(self):
        super.method1()#when ever we want to call instance method into the
        #sub class from the super class.
        print("method-2 of sub class.")

#calling
sub=sub()
sub.method2()
l()

print("doing same thing to the @static methods.")
class super:
    @staticmethod
    def method1():#static method
        print("Static method-1 of class super")
        l()
class sub:
    def method2(self):#instance method
    #calling static method-1
        super.method1()#using class name
        s=super()
        s.method1()#using object eference.
        print("method2 in sub class.")
#calling
sub=sub()
sub.method2()
l()




















































