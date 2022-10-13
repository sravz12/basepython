def sum(a,b):
    print("sum is",a+b)
def sub(a,b):
    print("sub is",a-b)
def div(a,b):
    print("div is",a/b)
def mul(a,b):
    print("mul is",a*b)
while True:
    print(1.,"addition")
    print(2.,"subtraction")
    print(3.,"division")
    print(4.,"multiplication")
    print(5.,'Break')
    ch=int(input("enter the choice"))
    if ch==5:
        break
    a=int(input("enter the number"))
    b=int(input("enter the second number"))
    if ch==1:
        sum(a,b)
    elif ch==2:
        sub(a,b)
    elif ch==3:
        div(a,b)
    elif ch==4:
        mul(a,b)
    else:
        print("wrong choice")
        break


