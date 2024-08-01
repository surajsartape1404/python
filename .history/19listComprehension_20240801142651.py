# list Comprehension
# return type will always be []
# program 1

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

# program 2

numbers = [11,22,33,44,55,66]
e2 = [x+10 for x in numbers]
print(e2)

# program 3