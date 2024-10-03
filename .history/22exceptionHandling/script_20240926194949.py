
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


# try except else finally

# try:
#     x = 1/2
# except ZeroDivisionError:
#     print("you cannot divide by zero..")
# else:
#     print("no exception raised")
# finally:
#     print("this will always execute")

# finally block always execute irrespective of 
# exception raised or no exception raised


# program 6...........
# Raising the exception manually

# def check_age(age):
#     if age <= 18:
#         raise ValueError("age must be greater than 18")
#     return True

# try:
#     check_age(25)
#     print("success")
# except ValueError as e:
#     print(e)


# def check_age(age):
#     if age <= 18:
#         raise ValueError("age must be greater than 18")
#     return True

# try:
#     check_age(17)
#     print("success")
# except ValueError as e:
#     print(e)


# # program 7 
# Raising the exception
# # customized


class UnderAgeError(Exception):
    pass

def check_age(age):
    if age <= 18:
        raise UnderAgeError("age must be greater than 18")
    return True

try:
    check_age(17)
    print("success")
except UnderAgeError as e:
    print(e)

class UnderAgeError(Exception):
    pass

def check_age(age):
    if age <= 18:
        raise UnderAgeError("age must be greater than 18")
    return True

try:
    check_age(24)
    print("success")
except UnderAgeError as e:
    print(e)

# # program 8
# # assert 

# def checkPositive(x):
#     assert x > 0 ,"x must be positive"


# try:
#     checkPositive(-1)
#     print('positive number...')
# except AssertionError as e:
#     print(e)


# # program 9
# try:
#     with open('filetext2.txt',"r+") as f:
#         c = f.read()
#         print(c)
# except FileNotFoundError:
#     print("File not found")

