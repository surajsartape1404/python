info = {
    "firstName":"suraj",
    "lastName":"sartape",
    "age":25,
    "age":73
}

print(type(info))
# allows duplicate property value 
print(info)
# how to find particular property exist or not
# in operator

print("age" in info)
print("Age" in info)
# how to loop over dictionary

for prop in info:
    print(prop)
    print(info[prop])

# methods of dictionary
# program 1
vehicle = {
    "color":"red",
    "regNo":123,
    "city":"pune"
}

# get()

e = vehicle.get('Color')
print(vehicle['Color'])
print(e)
print("hello")

# program 2

vehicle = {
    "color":"red",
    "regNo":123,
    "city":"pune"
}
info = {
    "firstName":"chinmay",
    "lastName":"rajat"
}

# clear()
# vehicle.clear()
# print(vehicle)

# update()
info.update(vehicle)
print(info)

# copy()

info = {
    "firstName":"chinmay",
    "lastName":"rajat"
}
# info2 = info
# info2["firstName"] = "sneha"
# print(info2)
# print(info)

# copy()
info2 = info.copy()
print(info2)
info2['lastName'] = "dani"
print(info)
print(info2)

#pop()
#popitem()
info = {
    "firstName":"chinmay",
    "lastName":"deshpade",
    "age":34,
    "city":23
}

print(info)
info.pop('firstName')
print(info)
info.popitem()
print(info)