# program 1

# p1 = open('suraj-sartape.jpg','rb')
# p2 = open('shubham.png','wb')
# bytes = p1.read()
# p2.write(bytes)
# p1.close()
# p2.close()

# program 2

with open('.txt','w') as p:
    p.write('I am learning js...')
    p.write('I am learning python...')

    with open('p.txt','r')as p:
        a = p.read()
        print(a)