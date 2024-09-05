# program .txt text file
# mode ---->  read, write, append
# creating the object of file & opening in write mode 

f = open('dayone.txt','w')

# writing into the file
f.write("I am learning python")

# close the file
f.close()


# program 2
# open the file in read mode
f = open('day.txt','r')