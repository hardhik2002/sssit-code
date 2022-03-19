#practicing sssit regular expressions.
import re
pattern=re.compile("h\w\w\w")
target=pattern.match("hari kari teri")#only prints the first word in the string
print("The matched object is:",target)
print("_"*80)


pattern=re.compile("h\w\w\w")
target=pattern.search("kari hari mari huri hlori")#entire string lo first appearence ni matramey print chestadhi
print("The matched object is:",target)
print("_"*80)


pattern=re.compile("h\w\w\w")
target=pattern.findall("kari hari mari huri hlori")#The output gives in the form of list.
print("the matched words are:",target)
print("_"*80)


#alternative ways for match()|search()|findall()
#practicing match()
match=re.match("h\w\w\w","hari kari teri")
print("The match is:",match)
print("_"*80)
#trying same with input()
input=input("Enter your four characters:")
match=re.match("h\w\w\w",input)#This working fine.
print("the match is:",match)
print("_"*80)


#practicing search()
search=re.search("h\w\w\w","lari kari teri hari holi")
print("The searched one is:",search)
print("_"*80)

#practicing findall()
findall=re.findall("h\w\w\w","lari kari teri hari holi")
print("after applying findall:",findall)
print("_"*80)

#practicing the match() object.

match=re.match("m\w\w","mom dad mam sir anu")
print("match objects are:",match)
print("Match:",match.group())
print("starting index position of matched object:",match.start())
print("Ending index pos+1 of matched object:",match.end())
print("_"*80)
#practicing match() objects for digits.
"""dmatch=re.match("\d\d"," 222 34 56")
print("match object is:",dmatch)"""
#deniki expected output ravatla.

#practicing finditer().
finditer=re.finditer("m\w\w","mom dad mam sir mad anu")
print("finditer object is:",finditer)
print("-"*40)

for m in finditer:
    print(m)
   
    print("match object is:",m.group())
    
    print("starting index of the object:",m.start())
    
    print("Ending index:",m.end())
print("_"*80)

#working with pre defined pattern.

#using \d-only digit.
onlydigit=re.finditer("\d","a1 $7A *B")#\D-except digits.
for m in onlydigit:
    print("Matched object:",m.group())
    print("start Index is:",m.start())
    print("End index is:",m.end())
    print("-"*50)
print("_"*80)
#using \w-alpha numerical.
anum=re.finditer("\w","Hardhik2002 hardhik haneesha")
for m in anum:
    print("Matched object is:",m.group())
    print("strting Index is:",m.start())
    print("ending index is:",m.end())
    print("-"*50)






























































































