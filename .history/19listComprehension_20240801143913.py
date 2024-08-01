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

marks = [44,55,66,77,88,55,44,88]
above60 = []

#  for x in marks:
#     print(x)
#     if x > 60:
#         above60.append(x)
# print(above60)

# above602 = list(filter(lambda x:x>60,marks))
# print(above602)

e3 =[x for x in marks if x > 60]
print(e3)

e4 = [x for x in marks if x < 60]
print(e4)

# program 4

numbers2 = [11,22,33,44,55]

# status = []

# for x in numbers2:
#     if x % 2 == 0:
#         status.append("even")
#     else:
#         status.append("odd")
# print(status)

# [ternary:loop]
e5 = ["even" for x in numbers2 if x%2 == 0]
print(e5)
