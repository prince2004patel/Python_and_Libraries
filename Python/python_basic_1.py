
# name = input("what is your name? ")
# print("Hello " + name)

# birth_year = input("enter your birth year")
# 2004
# "2004"  both are different

# age = 2024 - int(birth_year)
# print(age)

# first = input("first:")
# "10"
# second = input("second:")
# "20"
# 1020 is not right
# sum = int(first) + int(second)
# print(sum)

# course = "python for beginners"
# print(course)
# print(course.replace("y","4"))
# print(course.upper())
# print("python" in course)

# print(10/3)
# print(10//3)
# print(10 ** 3)

# x = x+3
# x += 3

# x = 10 + 3 * 2
# print(x)
# x = (10 + 3) * 2
# print(x)

# price = 8
# print(price>5 and price<30)
# print(price>4 or price<4)

# temperature = 8
# if temperature>35:
#     print("it's a hot day")
#     print("drink plenty of water")
# elif temperature >= 25:
#     print("it's a nice day")
# elif temperature <= 10:
#     print("it's  a bit cold")
# print("done")

weight = int(input("weight:"))
unit = input("(K)g or (L)bs :")
if unit.upper() =="K":
    converted = weight / 0.45
    print("weight in lbs:" + str(converted))
else:
    converted = weight * 0.45
    print("weight in kgs:" + str(converted))

# i = 1
# while i <= 5:
#     print(i * "*")
#     i = i+1

# names = ["prince" , "param" , "dv" , "nakul" , "purv" , "prit" , "aksh"]
# print(names[2])
# print(names[0:3])

# number = [1,2,3,4,5]
# print(len(number))
# number.insert(0,0)
# print(number)
# number.append(6)
# print(number)
# print(len(number))

# number = [1,2,3,4,5]
# for item in number:
#     print(item)
#
# print("-------")
# i= 0
# while i< len(number):
#     print(number[i])
#     i=i+1

# numbers = range(5,10,2)
# for item in numbers:
#     print(item)
# print(numbers)

# numbers = (1,2,3,3)
# numbers [0]=10  tuples cannot change
