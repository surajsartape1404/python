# # program .txt text file
# # mode ---->  read, write, append
# # creating the object of file & opening in write mode 
# f = open('day.txt','w')

# # writing into the file
# f.write("I am learning python")

# # close the file
# f.close()


# # program 2
# # open the file in read mode
# f = open('day.txt','r')

# # read the file 
# e = f.read()
# # printing the string
# print(e)
# #closing the file
# f.close()


# #program 3
# # will overwrite the existing file
# f = open('day.txt','w')
# f.write("I am learning js")
# f.close()


# # program 4 
# # opening the file in append mode
# f = open('day.txt','a')

# # writing new line to file
# f.write("I am learning python  \n")

# # closing the file
# f.close()


# # f = open('day2.txt','a+')
# # e = input("please enter your name ..\n")
# # f.write(e +"\n")
# # e2 = f.read()
# # print(e2)
# # f.close()