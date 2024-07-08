a = 10
b = 50

if a > b:
    print("a is greater")
else:
    print("b is greater")



# ternary operator
print("a is greater") if a > b else print("b is greater")

# program 2
age = 17
e = "can drive" if age >= 18 else "cannot drive"
print(e)

# loop 
# for loop  and while loop
print(1)
print(2)
print(3)
print(4)
print(5) 

#range(startValue,EndValue,StepSize)
# by default start value is 0
#range(10)--- range(0,10)

# program 1
for x in range(10):
    print(x)

for x in range(1,9):
    print(x)

# print 1 to 3
for x in range(1,4):
    print(x)

# program 2
#print "hello" 3 types
for x in range(0,3):
    print("hello")
for x in range(1,4):
    print("hello")
for x in range(3):
    print("hello")

# program 3
# print 1 to 5
for x in range(1,6):
    print(x)

# program 4
# range(startValue,Endvalue(not included),stepSize)
# range(1,5,1)

# 1  2  3  4  5
for x in range(1,6,2):
    print(x)

# program 5
for x in range(2,21,1):
    print(x)

# program 6
for x in range(3,31,3):
    print(x)

# program 5
# print 5 to 1
for x in range(5,0,-1):
    print(x)

# print 3 to 1 
for x in range(3,0,-1):
    print(x)

# print table of 3 in reverse
for x in range(20,1,-2):
    print(x)

# print table of 5 in reverse
for x in range(50,4,-5):
    print(x)

