# date: 11-07-2024


# string methods 
firstName = "chinmay"
print(type(firstName))

e1 = firstName.upper()
print(e1)

lastName = "Deshpande"
e2 = lastName.lower()
print(e2)

middleName = "shirish"
e3 = middleName.capitalize()
print(e3)

# upper() , lower() , capitalize()

# program 2

firstName = "rahul"
e4 = firstName.startswith("r")
e5 = firstName.startswith('ra')
print(e4)
print(e5)

e6 = firstName.endswith('l')
e7 = firstName.endswith('Ul')
print(e6)
print(e7)

# program 3
firstName = " chinmay "
print(len(firstName))

e5 = firstName.strip()
print(len(e5))

e6 = firstName.lstrip()
print(len(e6))

e7 = firstName.rstrip()
print(len(e7))

# program 4
str = "123213123123"
e8 = str.isdigit()
print(e8)

str2 = "amol"
e9 = str2.isalpha()
print(e9)

str3 = "mayur123"
print(str3.isalnum())


str3 = "123"
print(str3.isalnum())

str3 = "aaaa"
print(str3.isalnum())

str3 = "aaaa #"
print(str3.isalnum())


#program 5
str = "i am learning python"
e10 = str.replace("python","js")
print(e10)

str2 = "Hello"
e11 = str2.lower()
print(e11)