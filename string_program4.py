str=input("enter the string")
str1=str.lower()
vowel=0
space=0
con=0
d=0
for i in str:
    if i in 'aeiou':
        vowel+=1
    elif i==" ":
        space+=1
    elif i in '0123456789':
        d+=1
    else:
        con+=1
print("number of vowels",vowel)
print("number of space",space)
print("number of consonants",con)
print("number of digits",d)


