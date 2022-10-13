n=int(input("enter the number"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for k in range(1,i+1):
         print("*",end=" ")
    print()