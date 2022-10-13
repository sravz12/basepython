#Regular expressions --> (search,match,findall,sub)

# import re
# str="python programming"
# result=re.search('python',str)   #re.search(pattern,string)
# if result:
#     print("pattern is exist")
# else:
#     print("pattern not exist")


# import re
# str="python programming is fun"
# result=re.match('fun',str)        #re.match(pattern,string) it only match the beginning
# if result:
#     print("pattern is exist")
# else:
#     print("pattern not exist")

# import re
# zipcode='123-22 ssaf 2'
# result=re.findall('\d',zipcode)        #re.findall(pattern,string)
# print(result)


# import re
# zipcode="122-2 aas 3"
# result=re.sub('\D','@',zipcode)        #re.sub(pattern,substitute,string)
# print(result)


#Task
import re

pas=input("Enter the password")
if len(pas)<=6 or len(pas)>=16:
    print("inavalid password")
elif not re.search('[a-z]',pas):
    print("invalid password")
elif not re.search('[A-Z]',pas):
    print("invalid password")
elif not re.search('[0-9]',pas):
    print("invalid password")
elif not re.search('[@&$]',pas):
    print("invalid password")
else:
    print("password is correct")

