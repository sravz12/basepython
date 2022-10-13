#dictionary concept

# dict={}
# dict['hello']=1
# dict['are']=3
# print(dict)
# dict['hello']=dict['hello']+1
# print(dict)

def wordcount(lst):
    dict={}
    for word in lst:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    print(dict)
f1=open('File3','r')
r=f1.read()
n=r.split()
wordcount(n)

# def wordcount(lst):
#     dict={}
#     for word in lst:
#         if word in dict:
#             dict[word]+=1
#         else:
#             dict[word]=1
#     for k,v in dict.items():
#         print(k,":",v)
# f1=open('File3','r')
# r=f1.read()
# n=r.split()
# wordcount(n)