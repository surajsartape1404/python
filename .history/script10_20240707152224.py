# create  / add
# update
# remove
# retrive 
#           0       1         2          3
cities = ["pune","mumbai","bangalore","kolkata"]
print(len(cities))
print(cities[0])

# update
cities[0]= "nagpur"
cities.extend(["kanpur","jaipur"])

# add
cities.append("wardha")

#delete
cities.pop()
cities.pop(2)
cities.remove("kanpur")


# dictionary
#         0          1        2   3
info = ["suraj","sartape",25,73]

infoB = {
    "firstName":"suraj",
    "lastName":"sartape",
    "rollNo":25,
    "age":73
}

# dict does not stores the value by index
#print(infoB[0])

# retrive 
print(infoB["firstName"])
#update
infoB["firstName"]= "sagar"
print(infoB)
# add 
infoB['city'] = "latur"
print(infoB)
# delete
infoB.pop("age")
print(infoB)


vehicle = {

    "type":"sedane",
    "model":"G3",
    "companyName":"Audi"
}

# check particular property exist
print("model" in vehicle)

# retrive 
print(vehicle['model'])

#update
vehicle['model'] = "G4"
print(vehicle)

#add 
vehicle['regNo'] = "123"
print(vehicle)

#delete
vehicle.pop("model")
print(vehicle)

#in operator
print("type" in vehicle)

# looping over dictionary

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":34
}

for prop in student:
    print(prop,student[prop])
