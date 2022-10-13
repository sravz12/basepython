#exception - upnormal errors/conditions occurs during execution of programs

a=int(input("enter the first number"))
b=int(input("enter the second number"))
try: #suspected code
    div=a/b
    print(div)
except: #code for handling exception
    print('not give 0 as second value')