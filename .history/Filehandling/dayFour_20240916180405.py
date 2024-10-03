# program 1

# p1 = open('suraj-sartape.jpg','rb')
# p2 = open('shubham.png','wb')
# bytes = p1.read()
# p2.write(bytes)
# p1.close()
# p2.close()

# program 2

# with open('p2.txt','w') as p:
#     p.write('I am learning js...')
#     p.write('I am learning python...')

#     with open('p2.txt','r')as p:
#         a = p.read()
#         print(a)

# python object -----> binary file----->serialization
# binary file -----> python object -----> deserialization

class Employee:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName )

a = Employee("Suraj","Sartape")

import pickle
f= open('emp.data')