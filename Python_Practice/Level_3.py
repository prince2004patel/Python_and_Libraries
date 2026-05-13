### LEVEL 3

## 1. Create a list called fruits containing: "apple", "banana", "mango" Print the list.

# fruits = ["apple", "banana", "mango"]
# print(fruits)

## 2. Using list of numbers, print: The first element The last element The third element

# numbers = [10, 20, 30, 40, 50]
# print("The first element is:", numbers[0])
# print("The last element is:", numbers[-1])
# print("The third element is:", numbers[2])

## 3. Using list of fruits, Add one new fruit using append() Remove one fruit using remove()

# fruits = ["apple", "banana", "mango"]
# print("Original list:", fruits)
# fruits.append("orange")
# print("After adding a new fruit:", fruits)
# fruits.remove("banana")
# print("After removing a fruit:", fruits)

## 4. Using list of colors, Print:First three colors Last two colors Every second color

# colors = ["red", "green", "blue", "yellow", "purple"]
# print("First three colors:", colors[:3])
# print("Last two colors:", colors[-2:])
# print("Every second color:", colors[::2])

## 5. Using list of animals, Use a for loop to print each animal on a new line.

# animals = ["cat", "dog", "rabbit", "elephant"]
# for animal in animals:
#     print(animal)

## 6. Create a tuple containing five numbers. Print: The tuple Its length The second element

# numbers_tuple = (1, 2, 3, 4, 5)
# print("The tuple:", numbers_tuple)
# print("Its length:", len(numbers_tuple))
# print("The second element:", numbers_tuple[1])

## 7. Create two sets: Print: Union Intersection Difference (set1 - set2)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}   
# print("Union:", set1.union(set2))
# print("Intersection:", set1.intersection(set2))
# print("Difference (set1 - set2):", set1.difference(set2))

## 8. Create a dictionary to store: Name Age City Print the dictionary.

# person = {
#     "Name": "Prince",
#     "Age": 21,
#     "City": "Gandhinagar"
# }
# print("The dictionary:", person)

## 9. Using the dictionary, print name of the person, update the age to 22 and add new key-value pair "Gender":"Male"

# person = {
#     "Name": "Prince",
#     "Age": 21,
#     "City": "Gandhinagar"
# }
# print("Name of the person:", person["Name"])
# person["Age"] = 22
# person["Gender"] = "Male"
# print("Updated dictionary:", person)

## 10. Create a dictionary for a student with: Name Marks in Python Marks in Statistics Marks in Machine Learning
## Then: Print all details Calculate the average marks Print the average

# student = {
#     "Name": "Prince",  
#     "Marks in Python": 85,
#     "Marks in Statistics": 90,
#     "Marks in Machine Learning": 95
# }
# print("Student details:", student)
# average_marks = (
#     student["Marks in Python"] + 
#     student["Marks in Statistics"] + 
#     student["Marks in Machine Learning"]) / 3
# print("Average marks:", average_marks)
