"""Day One"""
# # important built-in functions

# char_fun=chr(66)
# ord_fun=ord("V")
# len_fun=len("ismail")

# print("------------------")
# print(char_fun)
# print("------------------")
# print(ord_fun)
# print("------------------")
# print(len_fun)
# print("------------------")



# name="ismail"
# age=21
# college="Benha University"
# country="Egypt"
# gender="male"

# print(f"My name is {name}, I am {age} years old, I study Engineering at {college}, I live in {country} and I am a {gender}")





# name=input("Enter Your Name: ")
# year_of_birth=int(input("Enter Your year of birth : "))
# age=2026-year_of_birth
# print(f"Your Name is : {name}, and Your Age is : {age}")



# type_variable=3.4
# print(type(type_variable))




# # Some Methods For Strings
# name = "ismail magdy ismail masoud ebeed"
# print(name.title())
# print(name.upper())
# print(name.lower())
# print(name.strip()) # act as trim in dart
# print(name.rstrip()) # act as trimRight in dart
# print(name.lstrip()) # act as trimLeft in dart



# # Method to convert decimal number to binary number
# number=2
# binary_number=bin(number)
# print(binary_number)


# nummber=1.7e5
# print(nummber)



# name="ismail"
# print(dir(name)) # to get all methods and attributes of the variable Object type



"""Day Two"""

# number=True
# number_two=False
# print(number and number_two) # and operator
# print(number or number_two) # or operator



# x=4
# y=5
# print(not x==5)


# print(bool(1))
# print(bool(0))



# double_python="python"*2
# print(double_python)

# print("e" in "ismail") # to check if the letter e is in the string ismail or not
# print(1 in [1,2,3,4,5]) # to check if the number 1 is in the list or not
# print("Hello" is "hello") # to check if the string Hello is the same as hello or not


# x=[1,2,3]
# y=[1,2,3]
# print(id(x)) # to get the memory address of the list x
# print(id(y)) # to get the memory address of the list y
# print(x is y) # to check if the list x is the same as the list y



# none=None
# print(type(none))# equal to null in dart




# Day Three

# # Tips at Python
# import this
# print(this.s)


# List
# numbers=[1,2,3,4,5,6,7,8]
# print(numbers)
# print(type(numbers))



# Another Shape of List
names=[
    "ismail",
    "ali",
    "ayman",
    "ahmed",
    "osama"]

# print(names[2])
# print(names[0].title()) # Make First Character Capital
# print(names[-1])
# print("My Name is "+names[0].title()+", and my Age is 21")



# names.append("mohammed")# To add element to List
# print(names)

names.insert(2,"shehab") # The value will be at the Index I Write
print(names)


# numbers=[2,4,5]
# print(numbers*2) # will repeat the numders at list, not multiply the numbers in 2
