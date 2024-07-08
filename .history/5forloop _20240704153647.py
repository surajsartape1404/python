# for 
# range(startValue,EndValue(not included),stepSize)
# startValue by default - 0
# stepsize by default -1 

# program 1
# print 1 to 3

for x in range(1,4):
    print(x)

for x in range(4):
    print(x)

# program 2
# print "hello"  3 times 
for x in range(3):
    print("hello")


# program 3
# print 1 to 5
for x in range(1,6):
    print(x)

# program 4
# print table of 2 
for x in range(1,6,2):
    print(x)

for x in range(2,21,2):
    print(x)

# program 5
# print 5 to 1
for x in range(5,0,-1):
    print(x)

for x in range(10,1,-1):
    print(x)

# table of 2 in reverse
for x in range(20,1,-2):
    print(x)

# table of 5 in reverse 
for x in range(50,4,-5):
    print(x)

# program 6
# break statement with for loop

for x in range(1,6): 
    if x == 3:
        break
    print(x) 

for x in range(1,6):
    print(x) 
    if x == 3:
        break

for x in range(5,0,-1): 
    if x == 3:
        break
    print(x) 

for x in range(30,2,-3):
    if(x == 15):
        break
    print(x)

# continue statement with for 
for x in range(1,6): 
    if x == 3:
        continue
    print(x) 



