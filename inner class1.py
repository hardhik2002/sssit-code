from line import *
#practicing inner class.
#inner class is also called as nested class.
"""
Example-1
"""
class employee:
    def set_employee(self):
        self.eno=input("Enter your number:")
        self.ename=input("Enter your name:")
    def get_employee(self):
        print("Employee number  is:",self.eno)
        print("Employee name is:",self.ename)
        l()
    class doj:
        def setdoj(self):
            print("Enter doj")
            self.dd=input("Enter DD:")
            self.mm=input("Enter MM:")
            self.yy=input("Entger YY:")
        def getdoj(self):
            print("doj is:  {}-{}-{}".format(self.dd,self.mm,self.yy))
            l()
#calling them.
e=employee()
e.set_employee()
d=e.doj()#idhi inner class kabatti malli e.doj() ani rasukunnamu.
d.setdoj()
l()
e.get_employee()
d.getdoj()
"""
example-25
"""
class student:
    def setstudent(self):
        self.sno=input("Enter sno:")
        self.sname=input("Enter sname:")

        self.d=self.dob()
        self.d.setdob()

        self.m=self.marks()
        self.m.setmarks()

    def getstudent(self):
        l2()
        print("sno is:",self.sno)
        print("sname is:",self.sname)
        
        self.d.getdob()
        self.m.getmarks()
    class dob:
        def setdob(self):
            print("Enter dob")
            self.dd=input("Enter DD:")
            self.mm=input("Enter MM:")
            self.yy=input("Enter YY:")
        def getdob(self):
            print("dob of student: {}-{}-{}".format(self.dd,self.mm,self.yy))
            
    class marks:
        def setmarks(self):
            self.s1=input("Enter sub1 marks:")
            self.s2=input("Enter sub2 marks:")
            self.s3=input("Enter sub3 marks:")
        def getmarks(self):
            l2()
            print("marks are:")
            print("sub1 marks:",self.s1)
            print("sub2 marks:",self.s2)
            print("sub3 marks:",self.s3)
            l()
            
#calling
s=student()
s.setstudent()
s.getstudent()

































