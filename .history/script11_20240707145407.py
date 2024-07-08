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
    "color":"black",
}
print(info)