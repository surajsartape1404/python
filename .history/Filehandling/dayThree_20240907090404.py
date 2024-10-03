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
    f.write("I am learning python + \n")
    f.close()
else:
    print("file not found")
    sys.exit()

# program 2
# number of lines
# number of words
# number of characters

f= open('day3.txt',"r")
cl = 0
cw = 0
cc = 0
for line in f:
    words = line.split(' ')
    cl = cl +1
    cw = cw + len(w)