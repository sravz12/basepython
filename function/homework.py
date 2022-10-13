# str=input("enter the string")
# n=int(input("enter the index"))
# new=str[:n]+str[n+1:]
# print(new)

#2)

def power(n,p):
    if p==0:
        return 1
    return n*power(n,p-1)
n=4
p=6
print(power(n,p))

