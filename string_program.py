s1=str(input('enter the string'))
s2=str(input("enter the substring"))
r=s1.find(s2)
if r!=-1:
    print("present at the location",r)
else:
    print('not present')


