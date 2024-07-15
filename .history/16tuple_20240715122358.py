# Date= 15-07-2024

tupleA = (11,22,33)
# tupleA[0] = 44
print(type(tupleA))
print(tupleA)

# Does tuple stores the value by index ?

tupleB = 11,12,13
print(type(tupleB))
print(tupleB)

print(12 in tupleB) 
print(22 in tupleB)
print(11 in tupleB)
print(15 in tupleB)

# loop using range

tupleC = ("suraj","sagar","shubham","chinmay")
print(tupleC)

for x in range(len(tupleC)):
    # print(x)
    print(tupleC[x])

# loop without using range

for item in tupleC:
    print(item)

# using while loop

i1 = 0
while i1 < len(tupleC):
    print(tupleC[i1])
    i1 = i1 + 1

# how to add element in tuple

fruits = ["apple","mango","banana","oranges"]
print(fruits)
print(len(fruits))
fruits.append("grapes")
print(fruits)

fruits = ("apple","mango","banana","oranges")
# print(type(fruits))
fruits = list(fruits)
fruits.append("grapes")
fruits = tuple(fruits)
print(fruits)