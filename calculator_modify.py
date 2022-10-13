while True:
    print("1.addition")
    print("2.subtraction")
    print("3.division")
    print("4.multiplication")
    print("5.exit")
    ch=int(input("enter the choice"))
    if ch==5:
        break
    elif ch>5:
        print('wrong input')
        break
    n = float(input("enter the first number"))
    m = float(input("enter the second number"))
    if ch==1:
        A=n+m
        print(A)
    elif ch==2:
        S=n-m
        print(S)
    elif ch==3:
        D=n/m
        print(D)
    elif ch==4:
        M=n*m
        print(M)
    else:
        print()
        break





