class Person:
    first_name = None
    last_name = None
    age = None
    roll_no = None

    # Methods
    def walk(self):
        print("I am walking")

    def talk(self):
        print("I am talking")

# object create
suraj = Person()
shubham = Person()

# retriving the property
print(suraj.first_name)
print(suraj.last_name)
print(suraj.age)
print(suraj.roll_no)

# calling on methods
suraj.talk()
suraj.walk()

# setting the properties values outside the class

suraj.first_name = "suraj"
suraj.last_name = 'sartape'
suraj.age = 26
suraj.roll_no = 70

print(suraj.first_name)
print(suraj.last_name)
print(suraj.age)
print(suraj.roll_no)

# shubham

print(shubham.first_name)
print(shubham.last_name)
print(shubham.age)
print(shubham.roll_no)

shubham.talk()
shubham.walk()

shubham.first_name = "shubham"
shubham.last_name = "sartape"
shubham.age = 28
shubham.roll_no = 65

print(shubham.first_name)
print(shubham.last_name)
print(shubham.age)
print(shubham.roll_no)

# setting the properties values at the time of object creation

class Person:
    #constructor
    def __init__(self,fn,ln,age,rollNo):
        self.firstName = fn
        self.lastName = ln
        self.age = age
        self.rollNo = rollNo
    
    def display_name(self):
        print(self.firstName + self.lastName)

suraj = Person("suraj","sartape",26,73)

print(suraj.firstName)
print(suraj.lastName)
print(suraj.age)
print(suraj.rollNo)

# calling the method
suraj.display_name()

shubham = Person("shubham","sartape",26,65)

print(shubham.firstName)
print(shubham.lastName)
print(shubham.age)
print(shubham.rollNo)


class PersonC:
    country = "india"
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def display_name(self):
        print(self.firstName + self.lastName)

    def changeCountry(self,nc):
        self.country = nc

suraj = PersonC("suraj","sartape")
suraj2 = PersonC("suraj2","sartape2")

print(suraj.firstName)
print(suraj.lastName)
print(suraj.country)

print(suraj2.firstName)
print(suraj2.lastName)
print(suraj2.country)

suraj2.changeCountry("bharat")
print(suraj2.country)
print(suraj.country)

# instance method - instance variables
class Person:
 # class variable
 country = 'india'

 def __init__(self,fn,ln,ag):
     self.firstName = fn
     self.lastName = ln
     self.age = ag