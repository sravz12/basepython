#largest among two numbers

lar=lambda x,y:x if x>y else y
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print("large is",lar(a,b))