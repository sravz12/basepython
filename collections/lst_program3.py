lst=input("enter the list").split()
print(lst)
even=[]
odd=[]
for i in lst:
    if int(i)%2==0:
        even.append(i)
    else:
        i=odd.append(i)
print("even numbers",even)
print("odd numbers",odd)



