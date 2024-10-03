# number of lines
# number of characters
# number of words

import os ,sys
fname = input("Enter the file:")
print(os.path)
print(fname)
print(os.path.isfile(fname))
if os.path.isfile(fname):
    f = open(fname,"a+")
    f.write("I am learning js + \n ")
    f.write("I am ")