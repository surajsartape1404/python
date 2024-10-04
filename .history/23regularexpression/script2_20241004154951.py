# a[\w]* = a an ann (or) a.......
# [\w]====> [a-z A-Z 0-9]
# \b = blank space
# \d = digit(0,1,2,3,4,5,6,7,8,9)

# program 1............

import re
str = 'an apple a day keeps doctor away'
a = re.findall(r'a[\w]*',str)
print(a)

# program 2.............
# \b = blank space 

str2 = re.findall(r'\ba[\w]*',str)
print(str2)


# program 3.............
# \d = digit = 0,1,2,3,4,5,6,7,8,9

str3 = "This meeting will be conducted on 1st and 21st of every month"
b = re.findall(r'\d[\w]*',str3)
print(str3)
print(b)

c = re.findall(r'\d[\d]*',str3)
print(c)


# program 4............
# search with exact 5 character

str5 = "one two three four "