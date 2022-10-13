def fact(a):
    count=1
    for i in range(1,a+1):
        count=count*i
    print("factorial is",count)
fact(4)