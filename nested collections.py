#practicing Nested collections.

#list nested collection.we can add any collection
#inside of list.
list1=[10,[11,12,13],{"app","map","nap"},
("Hardhik","Haneesha"),{"Name":"Hardhik","Age":18}]
print("The list data is:",list1)
print("""the first item in list is:{}\n
the second item in list off second item:{}\n""".format(list1[0],list1[1][1]))
print("_"*80)




#practicing tuple()
t=([10,20,30],(1.1,2.2,3.3),{"aaa","bbb"},
   {"sno":101,"sname":"sai","sage":32})
for i in t:
    if isinstance(i,dict):
        for k,d in i.items():
            print(k,d,sep=":")
    elif isinstance(i,set):
        for j in i:
            print(j)
            
            














