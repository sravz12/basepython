l=int(input("enter the first limit"))
u=int(input("enter the last limit"))
for i in range(l,u):
    for j in range(2,i-1):
        if i%j==0:
            break
    else:
         print(i,end=" ")