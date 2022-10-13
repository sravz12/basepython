print("1. celcius to Farenheit")
print("2. Farenheit to celcius")
n=float(input("enter your choice"))
if n==1:
    c=float(input("enter the temparature in celcius"))
    f=9/5*c+32
    print("temparature in Farenheit",f)
elif n==2:
    f=float(input("enter the temparature in farenheit"))
    c=(f-32)*5/9
    print("Temparature in celcius",c)
else:
    print('invalid choice')