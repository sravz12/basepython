#file ->the collection of data --->(jpeg,ppt,pdf,doc)
#fileobject=open('filename','mode')
#mode
#r - read
#r+ - read,write
#w - write
#w+ - write,read
#a - append
#read - read the content from file
f1=open('File1','r')
# print("first location:",f1.tell())  #tell() is used to find the location
# print(f1.read(3))
# print("second location:",f1.tell())
# print(f1.read(3))
# print("third location:",f1.seek(0)) #seek() is used to move the location
# print(f1.read(3))
# print(f1.readline())     # read the one line
# print(f1.readlines())    #read complete lines
a=f1.readlines()           # without \n
for i in a:
    print(i.strip())       #strip is used to avoid the newline
f1.close()