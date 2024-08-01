# list Comprehension
# return type will always be []

birthYear = [1998,1997,1996,1995]
ages = []

# for x in birthYear:
#     print(x)
#     print(2024-x)
#     age=2024-x
#     ages.append(age)
#     print(ages)

age2 = list(map(lambda x : 2024-x,birthYear))
print(age2)
