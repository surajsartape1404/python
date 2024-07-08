#Day 3 conditioal statements

# one input and mulltiple outcomes 
# numT > 0  and numT <= 5. ----- 5 % discount
# numT > 5. and numT <= 10 ----- 10% discount
# numT > 10                ----- 20 % discount

# if condition:
#     pass

# program 1
numT = 15
if numT > 0 and numT <= 5:
    print("5 % discount")
if numT > 5 and numT <= 10:
    print("10 % discount")
if numT > 10:
    print("30% discount")
    
# program 2
ticket = -17
if ticket > 0 and ticket <= 5:
    print("5 % discout")
elif ticket > 5 and ticket <= 10:
    print("10 % discount")
elif ticket > 10:
    print("30 % discout")
else:
    print("incorrect input")
    
# program 3
marks = 56
if marks > 90:
     print("grade A")
if marks >= 75:
     print("grade B")
if marks >= 65:
     print("grade C")
    
# program 4
if marks > 90:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 65:
    print("grade C")
else:
    print("please try again")
    
# program 5

s = 8
t = 4

if s > t:
    print("s is greater")
else:
    print("t is greater")
    
a1 = 8
a2 = 60
a3 = 400

# program 6
if a1 > a2 and a1 > a3:
    print("a1 is greater")
elif a2 > a1 and a2 > a3:
    print("a2 is greater")
else:
    print("a3 is greater")