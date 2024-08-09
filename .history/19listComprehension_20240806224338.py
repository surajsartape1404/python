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

e6 = ["odd" for x in numbers2 if x%2 != 0]
print(e6)


# use ternary if more than one reference

e7 = ["even" if x%2 == 0 else "odd" for x in numbers2]
print(e7)




birthYear = [1989,1990,1992,1992]
ages = []

for x in birthYear:
   age =  2024 - x
   ages.append(age)
print(ages)

e = list(map(lambda x: 2024 - x,birthYear))
print(e)

#[expression : loop : condition(one condition)]
#[ternary[multiple contion]:loop]
print([2024 - x for x in birthYear])

# program 2
marks = [33,44,55,66,22,33,56]
above50 = []
for x in marks:
   if x >  50:
      above50.append(x)
print(above50)
      
above502 = list(filter(lambda x : x > 50,marks))
print(above502)
above503 = [x for x in marks if x > 50]

# program 3
numbers = [11,22,33,44,66,33]
evenOdd = []
for x in numbers:
   if x % 2 == 0:
      evenOdd.append("even")
   else:
      evenOdd.append("odd")
print(evenOdd)
print(list(map(lambda x:"even" if x % 2==0 else "odd",numbers)))
print(["even" if x % 2 == 0 else "odd" for x in numbers])

# program 4
numbersB  = [11,22,33]
total = 0
for x in numbersB:
   total = total + x
print(total)

from functools import reduce
print(reduce(lambda acc,el:acc+el,numbersB))