def l():
    print("_"*80)
def l2():
    print("-"*80)

'''
IS-A relationship
'''
class super:
    def method1(self):
        print("instance method-1 of class super.")
class sub(super):#inheritance.
    #manam ila parenthisis lo class name rastey adhi inheritance ayitadhi.
    def method2(self):
        #ippudu ikkada method2 lopala method1 ravali antey ila cheyyali.
        self.method1()
        print("instance method2 of sub class.")
        self.method1()#function lopala vadutunnam kabatti manam self.method1() ani rasam.

#calling
s=sub()
s.method1()
s.method2()
l()

print("doing same thing for classmethods and staticmethods")
print("also trying to write function inside a function.")
l2()

class super:
    def method1(self):
        print("instance method-1 of class super")
    
    @classmethod
    def method2(cls):
        print("classmethod method-2 of class super.")
    @staticmethod
    def method3():
        print("staticmethod method-3 of class super.")
class sub(super):
    def method4(self):
        print("instance method-4 of class sub")
        self.method2()#callin cls method inside a function
        self.method3()#calling static method inside a function
        #ila rayali antey compolsary inheritence jarigi vundali.
#calling
s=sub()
s.method4()
l()














































