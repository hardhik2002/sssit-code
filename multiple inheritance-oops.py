from line import *
"""
praccticing multiple inheritance.
a very important topic

"""

print("example-1")
l2()
class father:
    def fatherheight(self):
        print("Height is from father.")
class mother:
    def mothercolor(self):
        print("Color is from Mother")
class son(father,mother):
    def properties(self):
        self.fatherheight()
        self.mothercolor()
        print("qualification from son.")
#calling
son=son()
son.properties()
l()


print("example-2")
l2()

class grandpa:
    def house(self):
        print("House from grandfather.")
class father(grandpa):
    def car(self):
        print("car is from father.")
        self.house()

class son(father):
    def bike(self):
        print("from son bike")
        self.car()
#calling
s=son()
s.house()
l2()
s.car()
l2()
s.bike()
l()

print("example-3")
print("Student Application".center(145))
l2()
class person:
    def setPerson(self):
        self.name=input("Enter name:")
        self.city=input("Enter city:")
    def getPerson(self):
        print("Name is:",self.name)
        print("City is:",self.city)
class student(person):
    def setStudent(self):
        self.setPerson()
        self.course=input("Enter course:")
    def getStudent(self):
        self.getPerson()
        print("course is:",self.course)
#calling
s=student()
s.setStudent()
s.getStudent()
l()


































