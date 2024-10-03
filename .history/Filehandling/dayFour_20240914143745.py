# program 1

p1 = open('suraj-sartape.jpg','rb')
p2 = open('shubham.png','wb')
bytes = p1.read()
p2.write(bytes)
p1.close()
p2.close()