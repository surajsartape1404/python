
# program 1

# print("hello")
# x = int(input('Enter a number 1..?'))
# y = int(input('Enter a number 2..?'))
# print(x/y)
# print('Bye')

# program 2

try:
    x = int(input('Enter a number 1..?')) 
    y = int(input('Enter a number 2..?')) 
    print(x/y) 
except:
    print("error .....occured")
print("bye")


program 3 
print('hello')
try:
    x = int(input('Enter the number 1...?'))
    y = int(input('Enter the number 2'))
    print(x/y)
except ZeroDivisionError:
    print('please enter the correct input')
except ValueError:
    print('please enter the numbers ')
except:
    print('please enter the valid input')
print("bye")