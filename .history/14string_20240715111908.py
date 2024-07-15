# date: 10-07-2024

# string

firstName  = "chinmay"
fname = 'chinmay'
fn = """sarika"""
fn2 = '''poorva'''

print(firstName)
print(fname)
print(fn)
print(fn2)
print(type(fname))


# program 1
# str stores the value by index 
city = "pune"
print(city[0])

# 0     1    2    3
# p     u    n    e
#-4    -3   -2    -1

# for loop 
for char in city:
    print(char)
# for loop with range 
for x in range(len(city)):
    #print(x)
    print(city[x])
# while loop
i1 = 0
while(i1 < len(city)):
    #print(i1)
    print(city[i1])
    i1 = i1 + 1

# program 3
#           0          1        2        3
names = ["chinmay",'shirish',"sarika","poorva"]
print(names[0])
names[1] = "sheerish"
print(names)

city2 = "nagpur"
city2[1] = "y"
city2 = 'wardha'

# program 4
str = "mumbai"
e = len(str)
print(e)

# program 5
city3 = "wardha"
e2 = city3.upper()
print(e2)

city4 = "Kanpur"
e3 = city4.lower()
print(e3)

city5 = "chandrapur"
e4 = city5.startswith('cha')
e5 = city5.startswith('c')
e6 = city5.startswith('C')

print(e4)
print(e5)
print(e6)


city6 = "jaipur"
e7 = city6.endswith('r')
e8 = city6.endswith('pur')
e9 = city6.endswith('R')
print(e7)
print(e8)
print(e9)
