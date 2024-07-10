info = {
    "firstName":"suraj",
    "lastName":"sartape",
    "age":25,
    "age":23
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
    "color":"white",
    "regNo":6211,
    "city":"latur"
}

# get()

e = vehicle.get('Color')
print(vehicle['city'])
print(e)
print("hello")

# program 2

vehicle = {
    "color":"black",
    "regNo":1911,
    "city":"nilanga"
}
info = {
    "firstName":"suraj",
    "lastName":"sartape"
}

# clear()

vehicle.clear()
print(vehicle)

# update()
info.update(vehicle)
print(info)

# copy()

info = {
    "firstName":"suraj",
    "lastName":"sartape"
}

# info2 = info

# info2["firstName"] = "sagar"

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
    "firstName":"suraj",
    "lastName":"sartape",
    "age":25,
    "city":"latur"
}

print(info)
info.pop('firstName')
print(info)
info.popitem()
print(info)



# vehicle = {
#     "color":"white",
#     "regNo":6211,
#     "city":"latur"
# }

# # get()

# e = vehicle.get('Color')
# print(vehicle['color'])
# print(e)
# print("hello")
