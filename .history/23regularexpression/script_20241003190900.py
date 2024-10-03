
# suraj-7229779575
# sagar-7845652145

# \w = [a-z A-Z 0-9]

# program 1........

import re 
str = "man boy sun run fun map cap"
obj = re.search(r'm\w\w',str)
print(obj.group())

# program 2..........

str2 = "man sad mad cat sat sun mate fate"
result = re.search(r's\w\w',str2)
if(result):
    print(result.group())

# print(result.group())

# str2 = "man sad mad cat sat sun mate fate"
# result = re.search(r'p\w\w',str2)
# if(result):
#     print(result.group())
# else:
#     print("code error")


# program 3...........

str2 =  "man sad mad cat sat sun mate fate 123 1234"
listA = re.findall(r's\w\w',str2)
print(listA)

listB = re.findall(r'\w\w\w',str2)
print(listB)

listC = re.findall(r'm\w\w\w',str2)
print(listC)

listC = re.findall(r'\w\w\w\w',str2)
print(listC)

listD = re.findall(r'm\w\w',str2)
print(listD)


# program 4.......

str3 = "python  is good language"
a = re.match(r'p\w\w',str3)
print(a)
print(a.group())


# program 5..........

# \+ not [a-z A-Z 0-9]
