#linear search
def linearsearch(lst,key):
    for i in lst:
        if i==key:
            print("key found at the position",lst.index(i)+1)
            break
    else:
        print("not found")
lst=[1,2,3,4,5,6,7]
key=4
linearsearch(lst,key)