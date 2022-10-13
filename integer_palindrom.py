n=int(input("enter the number"))
str1=str(n)
str2=str1[::-1]
print(str2)
if str2==str1:
    print("it is palindrome")
else:
    print("not palindrom")