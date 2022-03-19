def l():
    print("_"*80)
#practicing types of parameters.
#positional arguments.


def info(name,roll):
    print("My name is:",name)
    print("My roll number is:",roll)
    l()

info("Hardhik",35)

#keyword arguments.
def my_info(name,age):
    print("My name is:",name)
    print("My age is:",age)
    l()
my_info(name="Hardhik",age=18)

my_info(age=18,name="Hardhik")


#positional only arguments.

#The parameters which are declared left side of / called
#positional only arguments.


def my_pos(name,roll,/):
    print("Name is:",name)
    print("Roll is:",roll)
    l()
my_pos("Hardhik",45)

#keyword only arguments.

#te arguments which are declared right side of the *
#called keyword only arguments.
def my_key(*,name,age):
    print("Name is :",name)
    print("Age is:",age)
    l()
my_key(name="Hardhik",age= 90)

#mix off parameter and keyword only arguments.
def my_mix(a,b,/,c,d,*,e,f):
    print("a is:{}\nb is:{}\nc is:{}\nd is:{}\ne is:{}\nf is:{}"
          .format(a,b,c,d,e,f))
    l()
"""
a,b are positional only
c,d are both
e,f are keyword only
"""
my_mix(20,30,40,d=50,e=90,f=39)
my_mix(20,30,40,d=50,e=90,f=39)
#default arguments.
'''eg-1'''
def my_sum(x,y,z=100):
    s=x+y+z
    print("The sum is:",s)
    l()
my_sum(x=12,y=34)
#practicing varags.
#syn:my_var(*x)
'''
internally varags works like a tuple collection

'''
def my_varags(*x):
    print("The data is:",x)#now the x works like a tuple.
    l()
my_varags(10,"Hardhik")#same as tuple rules.

#kwargs is pending.




















