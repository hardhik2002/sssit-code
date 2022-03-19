##practicing the SSSIT notes date:22-07-2021
#practicing the different modes in print function.
txt1="Hardhik"
txt2="Hampika"
txt3="Haneesha"
print("Last kid was:%s\nFirst kid was:%s\nMiddle kid was:%s" %(txt1,txt2,txt3))
print("__________________________________")
print("He is:",txt1)
print("She is:",txt2)
print("She is:",txt3)
print("----------------------------------------------")
#doing by using format() function
print("He is:{}\nShe is:{}\nShe is:{}".format(txt1,txt2,txt3))
print("-----------------------------")
print("He is:{a}\nShe is:{b}\nShe is:{c}".format(a=txt1,b=txt2,c=txt3))
print("________________________________________________________")
a="Hardhik"
b=18
print("Hi there I am %s.and I am %i" %(a,b))
print("__________________________________________________________")

b=("Hi I am {x:}.and I am {y:} my salary is {z:}")
a=b.format(x="Hardhik",y=18,z=30000)#ee method ni values tesukonappudu vadukovochu
print(a)
print("_________________________")
a1=22
a2=33
a3=44
print(a1,a2,a3,sep="\n")
print("_________")
print(a1,a2,a3,sep="\\")
print("______________________________")
print(a1,end="\n")
print(a2,end="\t")
print(a3)
print("__________________________________")
print(a1,a2,a3,sep="\t")
print("_________________________")
print("Last kid was:%s\nFirst kid was:%s\nMiddle kid was:%s" %(txt1,txt2,txt3))
print("-----------------------------------------------------")
txt1=10
txt2=11
txt3=12
print("txt1 is:%i\ntxt2 is:%i\ntxt3 is:%i" %(a1,a2,a3))
print("_________________________________________________")
x="Hardhik"
y="Haneesha"
z="Hampika"
print(x,end='-')
print(y,end='-')
print(z)
print("__________________________________________________")
print(x,y,z,end='')
print("=====================================================")
print("___________________________________________________________")
myval="Valkal"
hisval="Harish"
print("%s" %hisval)
print("%s" %myval)
print("____________________________________________________________")
##practicing F strings
print(f"{myval}")
print(f"%s is good boy" %hisval)
print("_______________________________________________________________")

x="Valkal"
y="Anu"
z="Hemu"
print("He is:{}\nShe is:{}".format(x,y))
print("____________________________________________________________________")
print("Husband is:{}\nWife is:{}\nBrother is:{}".format(x,y,z,end="\n"))##ee method lo manki new line ravatla
##soo manam txt middle loney "\n" ni add cheyyali.
print("____________________________________________________________________")
print("hardhik is a good boy.\nHe loves coding.")
print("Hardhik is a bad boy.{}He never loves hima.{}He is very bad boy.".format("\n","\n"))
print("____________________________________________________________________")
'''So we can print a new line in these many steps'''















































