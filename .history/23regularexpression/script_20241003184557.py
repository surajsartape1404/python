
# suraj-7229779575
# sagar-7845652145

# \w = [a-z A-Z 0-9]


import re 
str = "man boy sun run fun map cap"
obj = re.search(r'm\w\w',str)
print(obj.group())


