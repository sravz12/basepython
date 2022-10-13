#map_function
#map(fun,seq)
# def mul(n):
#     return n*n
# num=[1,2,3,4,5,6]
# result=map(mul,num)
# print(list(result))
#lambda
# num=[1,2,3,4,5,6]
# result=map(lambda n:n*n,num)
# print(list(result))

# num1=[1,2,3,4]
# num2=[5,6,7,8]
# result=map(lambda x,y:x+y,num1,num2)
# print(list(result))

# fruits=['apple','orange','mango']
# result=map(len,fruits)
# print(list(result))

fruits=['apple','orange']
result=map(list,fruits)
print(list(result))


