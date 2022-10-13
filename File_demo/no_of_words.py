# f1=open('File1','r')
# read=f1.read()
# n=read.split()
# print(n)
# c=0
# for i in n:
#     c=c+1
# print(c)

f1=open('File1','r')
read=f1.read()
n=set(read.split())
print(n)
c=0
for i in n:
    c=c+1
print(c)
