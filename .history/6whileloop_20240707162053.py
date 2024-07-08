# program 1
# initialization 
#while(condition):
    # statements 
    # increment / decrement

# 
# program 1
i1 = 1
while(i1 <= 3):
    print(i1) 
    i1 = i1 + 1 

# program 2
# print "hello" 3 times 
i2 = 1
while i2 <= 3:
    print("hello") 
    i2 = i2 + 1  

# program 3
# print 1 to 5
i3 = 1
while(i3 <= 5):
    print(i3)
    i3 = i3 + 1 

# program 4
# print 5 to 1
i4 = 5
while i4 >= 1:
    print(i4)
    i4 = i4 -1

#program 5
# table of 2 using while loop
i5 = 2
while i5 <= 20:
    print(i5)
    i5 = i5 + 2

#program 6
#table of 5 in reverse
i6 = 50
while i6 >= 5:
    print(i6) 
    i6 = i6 - 5  

# program 7
# break statement with while loop
i7 = 1
while i7  <= 5:
    if i7 == 3:
        break
    print(i7) 
    i7 = i7 + 1 

i7 = 1
while i7  <= 5:
    print(i7)  
    if i7 == 3:
        break
    i7 = i7 + 1 

i8 = 1
while i8 <= 5:
    if i8 == 3:
        i8 = i8 + 1 
        continue
    print(i8)  
    i8 = i8 + 1  