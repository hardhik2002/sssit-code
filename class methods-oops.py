#defining a line
def l():
    print("_"*80)

#practicing class methods.
    
'''
example-1

'''
class sample:
    def method1(self):
        print("Ins mtd-1")
        print("self is:",self)
    @classmethod
    def method2(cls):
        print("cls mtd-2")
        print("cls is:",cls)

#calling
s=sample()
s.method1()
sample.method2()
l()
'''
example-3

'''
class sample:
    x=222#static variable
    def method1(self):#instance method
        self.y=111#instance field
    def method2(self):#instance method
        self.y=self.y+sample.x
        print("result is:",self.y)
    @classmethod
    def method3(cls):
        print("static variable x:",cls.x)


#calling
s=sample()
s.method1()#calling instance method
s.method2()#calling instance method
sample.method3()
l()













































