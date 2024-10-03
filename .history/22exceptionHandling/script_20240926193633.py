
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

# print('hi')
# try:
#     x = 1/0
# except ZeroDivisionError:
#     print("you can't divide by zero")

# program 2...........

# try:
#     x= int(input('please enter a number 1..:'))
#     y= int(input('please enter a number 2..:'))
#     print(x/y)
# except ValueError:
#     print('value error occured')
# except ZeroDivisionError:
#     print('cannot divide by zero')
# except Exception as e:
#     print('any exception not known')
#     print(e)

# program 3..........
# Generic wat of raising exception

# try:
#     numbers = [11,22,33,44]
#     x= int(input('please enter a number 1..:'))
#     y= int(input('please enter a number 2..:'))
#     print(x/y)
#     print(numbers[5])
# except ValueError:
#     print('value error occured')
# except ZeroDivisionError:
#     print('cannot divide by zero')
# except Exception as e:
#     print('any exception not known')
#     print(e)

# program 4........
# try except else

# try:
#     x = int('a')
#     print("hello")
# except ValueError:
#     print("A value error occured")
# except Exception as e:
#     print(e)
# else:
#     print("i will run if no exception is raised")


# try:
#     x = int(5)
#     print("hello")
# except ValueError:
#     print("A value error occured")
# except Exception as e:
#     print(e)
# else:
#     print("i will run if no exception is raised")

# program 5..........