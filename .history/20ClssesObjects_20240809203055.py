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