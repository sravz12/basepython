#recursion ->a function call by itself
#factorial of number
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)   #4*fact(3)
print(fact(4))