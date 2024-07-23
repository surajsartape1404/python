# Date = 16-07-2024

# sets in python

# a = 10
# print(a)
# print(type(a))

# b = 12.3
# print(b)
# print(type(b))

# c = "chinmay"
# print(c)
# print(type(c))

# d = [11,22,33,44]
# print(d)
# print(type(d))

# e = {
#     "firstName":"suraj",
#     "lastName":"sartape"
# }
# print(e)
# print(type(e))

# f = (1,2,3,4,5)
# print(f)
# print(type(f))

# set set set set set set set set set set set set set set set set 

setA = {11,22,33,44,55,66}
print(setA)

setB = {44,55,66,77,33,44,55}
print(setB)
print(66 in setB)
print(666 in setB)


# for
setC = {"suraj","sagar","shubham","ram"}
for item in setC:
    print(item)
print(len(setC))

setD = {11,22,33,44,55}
print(len(setD))

# methods

# program 1
setA = {11,22,33}
setA.add(55)
print(setA)


#program2

setA = {11,22,33}
setA.pop()      
print(setA)

setC = {11,22,33,44,55}
setC.remove(33)
print(setC)

setD = {"suraj","sagar","shubham","ram"}
setD.remove("sagar")
print(setD)
setD.pop()
print(setD)


# program 3
setE = {"suraj","sagar","shubham","ram"}
print(setE)
setF = setE
setF.remove("sagar")
print(setF)
print(setE)

setE = {"suraj","sagar","shubham","ram"}
setF = setE.copy()
setF.remove("ram")
print(setF)
print(setE)


# program 4
setH = {11,22,33,44,55,66,77,88,99,100} 
setH.clear()
print(setH)

#program5
setG = {33,44,55,66,77}
setG.update([99,200,1333])
setG.update((222,333,4444))
print(setG)

#program6
setA = {11,22,33}
setB = {44,55,66}
setC = setA.union(setB)
print(setC)

#program7
# intersection()
setA = {11,22,33,55}
setB = {33,44,55,66}
setD = setA.intersection(setB)
print(setD)

#program8
# intersectionUpdate()
setA.intersection_update(setB) 
print(setA)# {33,55}

#program9
# diffrence()
setA = {11,22,33}
setB = {44,55,66,33}

# print(setA.difference(setB))
# print(setB.difference(setA))

setA.difference_update(setB) # {11,22}
print(setA)

#program10
#symmetric_difference()
setA = {11,22,33}
setB = {44,55,66,33}
print(setA.symmetric_difference(setB))

setA = {11,22,33,66}
setB = {44,55,66,33}
setA.symmetric_difference_update(setB)
print(setA)


setA = {11,22,33}
setB = {11,22}

print(setA.issuperset(setB))
print(setB.issubset(setA))

# Sets
setC = {11,33}
setD = {44,22,11}
print(setC.isdisjoint(setD))