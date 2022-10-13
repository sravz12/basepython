n=int(input('enter the num'))
count=0
s=0
num=num1=n
while n>0:
    d=n%10
    count=count+1
    n=n//10
print(count)
while num>0:
    d=n%10
    s=s+d**count
    n=num//10
if num1==s:
    print('armstrong')
else:
    print('not armstrong')




