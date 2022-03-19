from line import *
#practicing object class.


"""
Super class for every class is object class

"""
class a:
    pass
class b(a):
    pass
print("does a is the sub class object?:",issubclass(a,object))
print("does b is subclass of a?:",issubclass(b,a))
print("b is the sub class object?:",issubclass(b,object))














