a = 10
print(a)
print(type(a))


b = 10.5
print(b)
print(type(b))


c = True 
print(c)
print(type(c))


d = "suraj"
print(d)
print(type(d))


# comparison operator 

# < , > ,<= , >= , == ,!=
# entity < entity ------ o/p boolean ---- true or false

print(7 > 3) 
print(7 < 3)  
print(7 >= 3) 
print(7 <= 3) 
print(7 >= 7)
print(7 <= 7) 
print(7 != 7) 
print(7 == 8)
print(8 == 8) 

# Logical operator

#and 

# true   and   true  --- true
# false  and   true  --- false
# true   and   false --- false
# false  and   false --- false 

print(6 == 6 and 8 != 7)
print(5 == 3 and 9 == 9)
print(5 == 5 and 8 == 7 )
print(8 == 7 and 5 == 4)

#or 

# true  or  true  ---- true 
# false or  true  ---- true
# true  or  false ---  true 
# false or  false ---  false

print(7 == 7 or 9 == 9)
print(7 == 8 or 9 == 9)
print(6 != 8 or 9 == 7)
print(8 != 8 or 9 != 9)


# not
# not true  --- false 
# not false --  true

print(not (7 == 3))
print(not (8 == 8))