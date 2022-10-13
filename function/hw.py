str=input("enter the string").split()
key=input("key")
for i in str:
    if len(i)>=int(key):
        print(i)