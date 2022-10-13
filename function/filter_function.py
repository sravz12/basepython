#filter function-> filter(fun,sequence)
# lst=[1,2,3,4]
# res=filter(lambda x:x%2==0,lst)
# print(list(res))

# lst=input("enter the list").split()
# print(lst)
# res=filter(lambda x:int(x)%2==1,lst)
# print(list(res))

# lst=input("enter the list").split()
# print(lst)
# res=filter(lambda x:int(x)%5==0,lst)
# print(list(res))

lst=input("enter the list").split()
print(lst)
res=filter(lambda x:int(x)>5,lst)
print(list(res))