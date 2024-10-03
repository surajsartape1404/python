# Penter the no. of student---->

# python object -----> binary file-----> serialization
# binary file -----> python object -----> deserialization


class Employee:
    def __init__(self,fn,ln) -> None:
        self.firstName = fn 
        self.lastName = ln 

    def display_name(self):
        print(self.firstName + self.lastName)


import pickle 
f = open('emp2.data','wb')
n = int(input('Enter the number of student'))
for x in range(n):
    fn = input('please enter firstName')
    ln = input('please enter lastName ')
    e = Employee(fn,ln)
    pickle.dump(e,f)
f.close()