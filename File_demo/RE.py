# import re
# f1=open('file_re','r')
# text=f1.readlines()
# for i in text:
#     result=re.search('you',i)
#     if result:
#         print(i)

# import re
# f1=open('file_re','r')
# text=f1.readlines()
# for i in text:
#     result=re.search(r'\bs.e\b',i)      #\b is stands for blank space & . read any character
#     if result:
#         print(i)

import re
f1=open('file_re','r')
text=f1.readlines()
for i in text:
    result=re.search(r'\bs\w*e\b',i)      #\w* read word charcters
    if result:
        print(i)

