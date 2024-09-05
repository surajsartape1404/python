# # program 1

# #open the file 
# q1 = open('filetext2.txt','w')
# # write into the file 
# q1.write("i am learning python")
# # closing the file
# q1.close()


# # program 2
# # open the file 
# q1 = open('filetext3.txt','w')
# # taking the input from users
# str = input("Enter you name :")
# # write into the file 
# q1.write(str)
# # closing the file
# q1.close()


# # program 3
# #open the file
# q3 = open('filetext3.txt','r')
# # read from the file
# str = q3.read()
# # console the content of file
# print(str)
# # close the file 
# q3.close()

# program 4

# user input for multiple names 
# when user input '@', exit the loop

f1  = open('names.txt','w')
print('please enter "@" to exist')
while(str != "@"):
    str = input('please enter multiple names :') # chinmay # suraj # "@"
    if str != "@":
        f1.write(str + "\n")
f1.close()