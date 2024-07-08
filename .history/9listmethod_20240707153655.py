# list 

names = ["chinmay","shirish","ninad","amol","satish"]
print(names)

print(type(names))

# loop
for x in range(len(names)):
    #print(x)
    print(names[x])

for item in names:
    print(item)

i1 = 0
while(i1 < len(names)):
    print(i1)
    i1 = i1 + 1

# methods 
#            0        1        2       3
# adding the element
fruits  = ["apple","mango","banana","chikoo"]
print(fruits)

fruits.append("papaya")
print(fruits)

fruits.insert(2,"grapes")
print(fruits)

# program 2
vegetables  = ["brinjal","potato","tomato","cabbage","cauliflower"]
# remove the last element
vegetables.pop()
print(vegetables)
# remove by index
vegetables.pop(2)
print(vegetables)
# remove by element name 
vegetables.remove("cabbage")
print(vegetables)

# program 3
numbers = [11,22,33,44,55,66]
numbers.clear()
print(numbers)

# program 4
cities = ["pune","mumbai","banglore","kolkata","chennai"]
cities.reverse()
print(cities)

cities.sort()
print(cities)

# program 5
marks = [11,22,33,44,55]
marksB = [55,66,77,88,99,100,66]
marks.extend(marksB)
print(marks)

e = marksB.count(66)
print(e)

numbersM = [11,22,33]
e = numbersM.copy()
e[0] = 111

numberB = numbersM
numbersM[1] = 111
print(numberB)
print(numbersM)

print(e)
print(numbersM)