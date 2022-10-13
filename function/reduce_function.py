#reduce(fun,seq)
# import functools
# lst=[1,2,3,4,]
# res=functools.reduce(lambda x,y:x+y,lst)
# print(res)


#home work
import functools
lst=[4,9,6,8]
lar=functools.reduce(lambda x,y:x if x>y else y,lst)
print(lar)
