from line import *
#practicing the files
#files-1
f=open('txt-file.txt',"w")
#attributes
print("file name is is:",f.name)
print("filemode is:",f.mode)
print("is file is closed:",f.closed)
#functions
print("is file readable:",f.readable())#w+ perithey it becomes readable too
print("is file writable:",f.writable())
f.close()
print("Is file is closed:",f.closed)
l()





























