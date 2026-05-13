### LEVEL 1

## 1. Write a Python program that prints your full name.

# print("Prince Patel")

## 2. Print the following on separate lines: Your city, Your country, Your dream job

# print("Gandhinagar \nIndia \nData Scientist")

## 3. Create variables for: name age country Then print them.

# name = "Prince Patel"
# age = 21
# country = "India"
# print(name, "\n", age, "\n", country)

## 4. Create variables of these types: Integer Float String Boolean Print each variable and its type using type().

# integer_var = 10
# float_var = 3.14
# string_var = "Hello World"
# boolean_var = True
# print(integer_var, type(integer_var))
# print(float_var, type(float_var))
# print(string_var, type(string_var))
# print(boolean_var, type(boolean_var))

## 5. Take two numbers and print: Addition Subtraction Multiplication Division

# num1 = 10
# num2 = 5
# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)

## 6. Ask the user to enter their name and print:

# name = input("Enter your name: ")
# print("Hello, " + name + " ! welcome to the world of Python programming.")

## 7. Ask the user for their birth year and calculate their current age.

# birth_year = int(input("Enter your birth year:"))
# current_year = 2026
# age = current_year - birth_year
# print("Your current age is:", age)

## 8. Store two numbers in variables and swap their values.

# a = 5
# b = 10
# print("Before swapping: a =", a, "b =", b)
# temp = a
# a = b
# b = temp
# print("After swapping: a =", a, "b =", b)

## 9. Take user input for age and convert it into an integer. Print the age and its type.

# age = input("Enter your age: ")
# print("before conversion, age is:", age, "The type of age is:", type(age))
# age = int(age)
# print("After conversion, age is:", age, "The type of age is:", type(age))

## 10. Ask the user for: Name Age City Then print a formatted introduction

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")
