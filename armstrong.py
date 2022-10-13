n=int(input('enter the num'))
sum=0
num=n
while n>0:
    d=n%10
    s=d**3
    sum=sum+s
    n=n//10
print(sum)
if num==sum:
    print('it is Armstrong')
else:
    print('not Armstrong')



