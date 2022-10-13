str=input("enter the string").split()
key=input("enter the key value")
for i in str:
    if len(i)>=int(key):
        a=i[::-1]
        print(a)
    else:
        print('error')


