import functools
lst=input("enter the list").split()
newlst=list(map(int,lst))
print(newlst)
even=list(filter(lambda x:int(x)%2==0,newlst))
odd=list(filter(lambda x:int(x)%2==1,newlst))
print(even)
print(odd)
sum=functools.reduce(lambda x,y:x+y,even)
final=functools.reduce(lambda x,y:x+y,odd)
print(sum)
print(final)