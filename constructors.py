#defining a line.
def l():
    print("_"*80)

#constoctors.
#we should compolsory define constroctor with
#def __init__(self):
#we can't define a constructor with our own names.
'''
example-1

'''
class test:
    def __init__(self):
         self.x=10
         self.y=20
    def getdata(self):
        print("x:",self.x)
        print("y:",self.y)
        l()
        
#calling
t=test()
t.getdata()



#practicing dir() function
#which is used to see default constructors.
class paper:
    pass
p=paper()
print("The default constructors are:\n",dir(p))
l()

'''
example-2:Finding the area of the circle.

'''

class area_circle:
    def __init__(self):
        self.rad=4
    def findarea(self):
        self.area=3.14*self.rad*self.rad
        print("The area of the circle:",self.area)
        l()

#calling
ac=area_circle()
ac.findarea()



































































