
# suraj-7229779575
# sagar-7845652145

# \w = [a-z A-Z 0-9]

# program 1

import re 
str = "man boy sun run fun map cap"
obj = re.search(r'm\w\w',str)
print(obj.group())

# program 2

# str2 = "man sad mad cat sat sun mate fate"
# result = re.search(r's\w\w',str2)
# if(result):
#     print(result.group())

# print(result.group())

str2 = "man sad mad cat sat sun mate fate"
result = re.search(r'\w\w',str2)
if(result):
    print(result.group())