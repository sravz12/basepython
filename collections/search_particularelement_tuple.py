#tuple1=(1,3,4,5,7,8)
item=input("item entered").split()
tuple1=tuple(item)
print(tuple1)
n=int(input("item to be searched"))
for i in tuple1:
    if int(i)==n:
        print("present")
        break
else:
    print("not present")