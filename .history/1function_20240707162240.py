x = 10
print(x)
x = 300
print(x)

# Arithmetic operation
# + , -  , * , / , %

a = 10
b  = 5

print(a+b) 
print(a-b)
print(a*b)
print(a/b) # 2.0
print(a%b) # 0



# single 
# This is single line comment in python

'''
    This is multi-line comment in python
'''
"""
    This is multi-line comment in python
"""

s = 8
t = 4

print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)


def Cal(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
Cal(9,3)
Cal(6,3)

# def - keyword
# Calculator - function name 
# x , y - parameter
# print(x+y) - statement - 1
# print(x-y) - statement - 2
# print(x*y) - statement - 3
# print(x/y) - statement - 4
# print(x%y) - statement - 5
# Calculator(9,3) # 9,3 - arguments


# function without parameter and with return type
def add():
    print(9+9)
add()
add()
add()
add()
add()

# function with parameter and without return 
def addA(x,y):
    print(x+y)
addA(12,4)
addA(11,4)
addA(9,3)

# function with parameter and with return type
def addC(x,y):
    return x+ y
e = addC(12,4)
print(e)
print(e + e)
print(e / 4)
print(e * 0.10)