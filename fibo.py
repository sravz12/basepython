# n=int(input("enter the limit"))
# f=0
# s=1
# t=0
# print(f,s,end=' ')
# for i in range(2,n+1):
#     t=f+s
#     f=s
#     s=t
#     print(t,end=' ')

n=int(input("enter the number "))
f=0
s=1
t=0
print(f,s,end=' ')
for i in range(2,n+1):
    t=f+s
    f=s
    s=t
    print(t,end=' ')
