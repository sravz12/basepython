#accumulate(seq,fun)

# import itertools
# lst=[1,2,3,4]
# res=list(itertools.accumulate(lst))
# print(res)

import itertools
lst=[1,2,3,4,5]
res=list(itertools.accumulate(lst,lambda x,y:x*y))
print(res)

