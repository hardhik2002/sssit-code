#int type casting
#float-->int()
x=1209.334
y=int(x)
print(y)
print(type(y))
print("________________________")

'''float to int is possible'''
#Trying out complex to int()
'''comp=(30+40j)
inti=int(comp)
print(inti)'''
#complex to int() is not posiible
#Trying out string to int()
'''x="Hardhik"
y=int(x)
print(y)'''
#It gives error becuase akkada manaki string
#place lo only number yee vundali.
#lekapote error vastundhi
'''x="20.83"
y=int(x)
print(y)'''
#by the way float kuda vundakudadhu
#only number yee vundali
x="20"
print("x is:",x)
print("x type:",type(x))
y=int(x)
print("y type:",type(y))
print("y is:",y)
#ila chestey error radhu
print("_________________________")
#trying out bool to int()
x=True
print("x value is:",x)
print("x type is:",type(x))
y=int(x)
print("y type is:",type(y))
print("y value is:",y)
print("__________________________")

#Trying out the float type casting
#int-->float
x=20
print("type of x is:",type(x))
print("original version of x:",x)
print("type of new version of x:",type(x))
print(  "new version of x:",float(x))
print("____________________________")
#int-->float is absolutly possible.
#complex-->float
'''x=(20+30j)
print(float(x))'''
#complex-->float is not possible
#bool-->float
print("bool-->float()")
x=True
print(float(x))
y=False
print(float(y))
#bool-->float is possble
print("_______________________________")
#str-->float()
print("str-->floar()")
string="8106507485"
print(float(string))
print("_________________________________")
#str-->float() is possible.
#String type casting.
#int-->str()
print("int-->str()")
x=10
y=str(x)
print(type(x),type(y),sep="-->")
print(x,y,sep="-->")
print("__________________________")
#complex-->str()
print("complex-->str()")
com=(10+90j)
str1=str(com)
print(type(x),type(y),sep="-->")
print(x,y,sep="-->")
#complex-->str() is possible
print("____________________________")
#bool-->str()
print("bool-->str()")
bol=True
str2=str(bol)
print(type(bol),type(str2),sep="-->")
print(bol,str2,sep="-->")
#bool-->str() is possible
print("______________________________")
#float-->str()
print("float-->str()")
flo=20.33
str3=str(flo)
print(type(flo),type(str3),sep="===")
print(flo,str3,sep="-->")
print("_______________________________________")















