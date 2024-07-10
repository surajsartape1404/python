# Date: 09-07-2024

info4 = {
    "firstName":"suraj",
    "lastName":"sartape",
    "rillNo":73
}

print(info4.items())
print(info4.keys())
print(info4.values())

for x in info4.values():
    print(x)

for x in info4.keys():
    print(x)

for x in info4.items():
    print(x)

info5 = {
    "firstName":"suraj",
    "lastName":"sartape",
    "rollNo":73
}

print(type(info5))
e = dict.fromkeys(["firstName","lastName","rollNo"])
print(e)

e = info5.setdefault('city')
print(e)





# // revision

info6 = {
     "firstName":"suraj",
    "lastName":"sartape",
    "age":25,
    "rollNo":73
}


e = info6.get("rollNo")
print(e)
info6.update({"city":"latur"})
info6.popitem()
info6.pop("age")

for k in info6.keys():
    print(k)

for k in info6.values():
    print(k)












