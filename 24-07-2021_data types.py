##25-07-2021data type practice.
##practicing the string and string manuculation.
##practicing string methods.
"""String is an immutable data type"""

#capitalize()
txt="hardhik is a good boy.he works very hard for improving his coding skills."
print(txt.capitalize())#It capitalize the only first letter of the sentence.
print(txt.casefold())#make string lower case.
#It is similar to lower()
print("__________________________________________________________")
txt="hardhik is a good boy.he works very hard for improving his coding skills."
x=txt.center(200)
print(x)

#it brings the string to the center position.
print("__________________________________________________________")
txt2="Haneesha is a good girl."
print(txt2.center(10,"_"))
#It brings the string to the string to the center position.
print("__________________________________________________________")
print(txt2.count("Haneesha",0,10))
#it is one of the important string methode.
#it countes the indexes in the given value.
print("__________________________________________________________")
print(txt2.endswith("."))#it tells the string what ends with.
print("__________________________________________________________")

txt="Hi I am Hardhik\t Reddy, And my salary is more than 30,000."
print(txt.endswith(",",0,20))
print(txt.expandtabs(20))#ee expandtabs() ki strind lo kanaka "\t" istey akkada tab space vastundhi.
#that too manam ichina value ni batti.
print(txt.find("e"))
#find() and index() both are same with aome differences.
#It writes only the first appearence.
print("__________________________________________________________")
abc="My Name is:{x}\nMy salary is:{y}"
print(abc.format(x="Hardhik",y=30000))
print("__________________________________________________________")
x="Hardhik"
y=30000

print("My Name is:{}\nMy salary is:{}".format(x,y))
print("My Name is- {}\nMy salary is- {}".format("Haneesah",30,000))
print("__________________________________________________________")

print("Linga Reddy family has {:<5} kids".format(3))#left align
print("Linga Reddy family has {:>5} kids".format(3))#right align
print("{:^100}Linga Reddy family has kids".format(" "))#center align
print("__________________________________________________________")
txt1="""{:^500}Hardhik is a good boy.
He aslo won't studies well.So
teachers are alwayas beating hardhik very rudly.
Oh god please help Hardhik."""
print(txt1.format(""))#oka multi string ni center loki tesuku ravadam ee
#method lo kudaratla.
print("__________________________________________________________")



print("""Hardhik is a good boy.
He aslo won't studies well.So
teachers are alwayas beating hardhik very rudly.
Oh god please help Hardhik.""".center(200))#ee method lo kuda manaki multi line string ravatla.

print("__________________________________________________________")

x="#eb4034"
print(x.isdecimal())#It written False.
print("__________________________________________________________")

my_list=["Hardhik","Haneesha","Hampika"]
print("Valkal".join(my_list))

print("__________________________________________________________")

my_dict={"Hardhik","Hampika","Haneesha"}
myseparator="Test"
x=myseparator.join(my_dict)#id every word manam ichina value tho saparete chestundhi.
print(x)
print("__________________________________________________________")

#this is 26-07-2021 practice.

txt="Hi hardhik."
mytranse=txt.maketrans("hardhik","Kardhik")#make trans arguments same lenth lo vundali.
#deeni badulu manam replace() vadochu inka better ga vuntundhi.
print(txt.translate(mytranse))#well.......ee topic lo konni doubts vunnayi clarify in sssIt.
txt1="Hi Sam."
x="Sam"
y="Joe"
mytranse=txt1.maketrans(x,y)
print(txt1.translate(mytranse))
txt2="Hi Joe."
mytranse=txt2.maketrans("Joe","Sam")#third parameter lo ichina words ni txt nunchi tesestundhi.
print(txt2.translate(mytranse))#translate() takes only one argument.
#replace() is also similare to this with some changes.
print("__________________________________________________________")

#practicing the shesi kumar sir's class notes.
#this notes code is in python IDLE.
#trying out the strip() method.
txt="   ____         banana               "
x=txt.strip(" _")
print("in all fruits I like",x)

print("__________________________________________________________")

txt="Hardhik"
print("Hi I am",txt)
print("__________________________________________________________")
txt1="Hi I am hardhik."
x=txt1.strip("Hi")
print(x)
print("__________________________________________________________")

txt2="Hardhik is a good boy."
y=txt2.strip(".").replace("good","bad")
print(y)
print("__________________________________________________________")

txt=",,,rrgg......banana......rrr"

x=txt.strip(",.gr")
print(x)
print("__________________________________________________________")


x=int(input("Enter rows:"))
for i in range(0,x):
    for j in range(0,i+1):
        print("#",end=" ")
    print()

print("__________________________________________________________")





























































































































































































