
# program 1..........

# print("hello")
# x = int(input('Enter a number 1..?'))
# y = int(input('Enter a number 2..?'))
# print(x/y)
# print('Bye')

# program 2..........

# try:
#     x = int(input('Enter a number 1..?')) 
#     y = int(input('Enter a number 2..?')) 
#     print(x/y) 
# except:
#     print("error .....occured")
# print("bye")


# program 3 ...........

# try:
#     x = int(input('Enter the number 1...?'))
#     y = int(input('Enter the number 2'))
#     print(x/y)
# except ZeroDivisionError:
#     print('please enter the correct input')
# except ValueError:
#     print('please enter the numbers ')
# except:
#     print('please enter the valid input')
# print("bye")

# program 4............

# try:
#     numbers = [11,22,33,44,55]
#     n = int(input('please enter the index..'))
#     print(numbers[n])
# except IndexError:
#     print("please correct the index number")
# finally:
#     print('i will always execute...')


# Next Day

# program 1..............

print('hi')
try:
    x = 1/0
except ZeroDivisionError:
    print("you can't divide by zero")

# program 2...........