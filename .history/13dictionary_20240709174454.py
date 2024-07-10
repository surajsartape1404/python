info4 = {
    "firstName":"suraj",
    "lastName":"sartape",
    "rollNo":25
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
    "rollNo":24
}


print(type(info5))
e = dict.fromkeys(["firstName","lastName","age","rollNo"])
print(e)

e = info5.setdefault('city','pune')
print(info5)

#[] ---> list
#{key:value} ---> dictionary
#()          ---> tuple
#{11,22,33}  ---> set


# revision 


info6 = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":34
}
#e = info6.get("rollNo")
#info6.clear()
#info6.update({"city":"pune"})
#info6.popitem()
#info6.pop("age")
# for k in  info6.keys():
#     print(k)

# for v in  info6.values():
#     print(v)

# for item in  info6.items():
#     print(item)

# info7 = info6.copy()
# print(info7)
# info7['firstName'] = "amit"
# print(info7)
# print(info6)

# e = dict.fromkeys(["color","type","model"])
# print(e)

info6.setdefault('language',"marathi")
print(info6)
print(info6)
