def Binarysearch(lst,key):
    mid=0
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]<key:
            low=mid+1
        elif lst[mid]>key:
            high=mid-1
        else:
            return mid
    return -1
lst=input("enter the digits").split()
lst.sort()
print(lst)
key=input("enter the key")
f=Binarysearch(lst,key)
if f==-1:
    print("key not found")
else:
    print("key is found",f+1)
