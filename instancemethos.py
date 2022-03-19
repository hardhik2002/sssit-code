#definig a line.
def l():
    print("_"*80)
#practicing instancemethods.

#example-1
class student:
    def setstudent(self,a,b,c):
        self.m1=a
        self.m2=b
        self.m3=c
    def findresult(self):
        if self.m1>34 and self.m2>34 and self.m3>34:
            print("Student is pass")
            l()
        else:
            print("student is fail")
            l()

#calling
s=student()
s.setstudent(100,40,50)
s.findresult()

#example-2
class biggest:
    def setdata(self,x,y):
        self.x=x
        self.y=y
    def findbiggest(self):
        if self.x>self.y:
            print("Biggest number is:",self.x)
            l()
        else:
            print("Biggest number is:",self.y)
            l()

#calling
b=biggest()
b.setdata(200,30)
b.findbiggest()


















