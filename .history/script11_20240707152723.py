# dictionary
# program1

info = ["suraj","sartape",7083646111,25,71]

dictA = {
    "firstname":"suraj",
    "lastname":"sartape",
    "age":25,
    "rollNo":71,
    "phoneNumber":7083646111
}

# retrive
q1 = dictA["firstname"]
print(q1)

q2 = dictA["phoneNumber"]
print(q2)

q3 = dictA["age"]
print(q3)

# update 
print(dictA["lastname"])
dictA["lastname"] = "patil"
print(dictA)

dictA['city'] = "latur"
print(dictA)

# delete
dictA.pop("age")
print(dictA)

# program2

info = {
    "color":"white",
    "type":"swift",
    "regNo":"6211",
}
print(info)
print("type"in info)


# methods

student = {
    "firstname":"suraj",
    "lastname":"sartape",
    "age":25,
    "rollNo":73
}
print(student)

# method
# get()
print("hello")
print(student["age"])
print(student.get('age'))
print("bye")

# clear()
student.clear()
print(student)

# copy()
info2 = {
    "firstname":"suraj",
    "lastname":"sartape",
    "age":25
} 
print(info2)
info3 = info2
info2['firstname'] = 'sagar'
print(info3)

info3 = info2.copy()
info3['firstName'] = 'shubham'
print(info3)
print(info2)
print(prop,info3[prop])




