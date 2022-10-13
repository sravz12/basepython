str=input("enter the string").split()
for i in str:
    if len(i)%2==0:
        print("even string is",i)
    else:
        print()
        break