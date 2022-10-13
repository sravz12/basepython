str1='i like grapes'
str2=str1.lower()
count=0
for i in str1:
    if i in 'aeiouAEIOU':
        count+=1
print(count)
print("count of a",str2.count('a'))
print("count of e",str2.count('e'))
print("count of i",str2.count('i'))
print("count of o",str2.count('o'))
print("count of u",str2.count('u'))


