# dictionary 
#          0          1           2       3  4

info = ["chinmay","deshpande",7709292441,34,56]

dictA = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":45,
    "phoneNumber":7709192441
}
print(type(dictA))
# dictionary does not stores the value by index
#print(dictA[0])

# program 2
# retrive 
q1 = dictA['firstName']
print(q1)
#update 
print(dictA["lastName"])
dictA["lastName"] = "dani"
print(dictA)
#property:value
dictA['city'] = "pune"
print(dictA)
#delete
dictA.pop("age")
print(dictA)

# program 2
# do dictionary allow same properties twice
info = {
    "color":"red",
    "type":"sedane",
    "regNo":123,
    "color":"blue"
}
print(info)

# check whether property exist in dictionary
print("Type" in info)

# methods

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":34
}
print(student)

# get()
print("hello")
#print(student['Age'])
print(student.get('Age'))
print("bye")

# student.clear()
# print(student)

#copy

info2 = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23
}

# print(info2)
# info3 = info2
# info2['firstName'] = 'tanmay'
# print(info3)
# print(info2)

info3 = info2.copy()
info3['firstName'] = "ninad"
print(info3)
print(info2)