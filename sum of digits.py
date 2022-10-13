n=int(input('enter the number'))
sum=0
while n>0:
    d=n%10
    s=d*d
    sum=sum+s
    n=n//10
print(sum)
