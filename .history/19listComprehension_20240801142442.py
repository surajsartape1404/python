# list Comprehension
# return type will always be []
program 1
birthYear = [1998,1997,1996,1995]
ages = []        #[26,27,28,29]

# for x in birthYear:
#     age=2024-x
#     ages.append(age)
#     print(ages)

# e1 = list(map(lambda x : 2024-x,birthYear))
# print(e1)

# [expression:loop:condition]
e2= [2024-x for x in birthYear]
print(e2)

