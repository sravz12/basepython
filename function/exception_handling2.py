try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    c=a/b
    print(d)
except ValueError:                                       #(ValueError,ZeroDivisionError): #possible
    print("you must enter a number")
except ZeroDivisionError:
    print("enter the second number other than zero")
except:
    print("all other errors handle error")
else:
    print("execute if there is no error")
finally:
    print("always execute")