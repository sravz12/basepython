#find largest among 3 numbers
def larg(a,b,c):
    if a>b and a>c:
        print("a is greater",a)
    elif b>a and b>c:
        print("b is greater",b)
    else:
        print("c is greater",c)
larg(2,3,4)