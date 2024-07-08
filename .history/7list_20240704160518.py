# list 

x = 10
print(x)

# list 

names = ["chinmay",'ram',"sham","sachin","amit"]
numbers = [11,22,33,44,55,66]
canDrive = [True, False , True , False]
info = ["chinmay","deshpande",7709192441]

print(names)
print(type(names))

x = 10 
print(type(x))

y = 10.5 
print(type(y))

c = "chinmay"
print(c)
print(type(c))

#           0        1       2        3
fruits = ["apple","mango","grapes","papaya"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])


# program 2
#           0        1         2        3
cities = ['pune',"nagpur","bangalore","kolkata"]
#           -4      -3       -2          -1
print(cities[-1])
print(cities[-2])


# program 3
# for loop with range and for loop with range
#            0          1         2           3          4
country = ["india","pakistan","bangladesh","srilanka","china"]
print(len(country))

for x in range(5):
    print(country[x])

#         0    1    2    3
state = ["MH","MP","UP","RJ"]
for x in range(len(state)):
    print(state[x])


# for loop without range
for x in state:
    print(x)

# loop over list - while loop
#             0       1      2        3
animals = ["tiger","lion","rabbit","snake"]
for x in range(len(animals)):
    print(animals[x])



    i1 = 0
while(i1 < len(animals)):
    print(animals[i1])
    i1 = i1 + 1