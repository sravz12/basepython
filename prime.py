n=int(input("enter the number"))
c=0
for i in range(1,n+1):
    n%i==0
    c+=1
if c==2:
    print("it is a prime number")
else:
    print('not prime number')






