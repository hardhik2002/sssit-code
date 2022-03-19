#defining a line
def l():
    print("_"*80)
    
#practicing instance fields.
#example--1

class sample:
    def method1(self):
        x=111
        self.y=222
        print("x value is:",x)
        '''print("Y value is:",y)'''#here we get an error.
        print("y value is:",self.y)
        l()

s=sample()
s.method1()
print("From outside")
print("y value is:",s.y)
l()
#example-2
class sample2:
    def method1(self):
        x=100
        self.y=200
        print("x value is:",x)
        print("y value is:",self.y)
    def method2(self):
        '''print("x value is:",x)'''#we are getting error.
        print("y value is :",self.y)
        l()
#calling
s=sample2()
s.method1()
s.method2()
l()

















































