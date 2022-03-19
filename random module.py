import random
print(random.randint(1111,9999),"One time password")
print("_"*50)
lst=["Hardhik","Haneesah","Hampika"]
for i in range(1,11):
    print(random.choice(lst))
print("_"*50)
#devoloping a small game.
nlist=["Hardhik","Haneesha","Hampika"]
print("Chose from:",nlist,"And guess the output")
gword=input("Guess the gorla kids name:")
rword=random.choice(nlist)
if gword==rword:
    print("The gussed one is correct:",rword)
else:
    print("Better luck nest time.")#It's working.
print("_"*50)




    
    


























