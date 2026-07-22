# name = "bro"
# print ("Hello, " + name)
# first_name = "Scholes"
# last_name = "Agostino"
# full_name = first_name + " " + last_name
# print ("Hello, " + full_name)


# age = 19
# age += 1
# print("Your age is: " + str(age))
## print(type(age))

# # # # # # # height = 523.4
# # # # # # # print("Your height is: " + str(height))
# # # # # # # print(type(height))


# # # # # # human = False

# # # # # # print("Are you really a human?: " + str(human))

# # # # # name = "bro"
# # # # # age = 23
# # # # # attractive = True
# # # # name, age, attractive = "bro", 23, True



# # # # print(name)
# # # # print(age)
# # # # print(attractive)
# # # Spongebob = Patrick = Sandy = Squidward =30
# # # print(Spongebob)
# # # print(Patrick)
# # # print(Sandy)
# # # print(Squidward)



# # name = "scholes"
# # print(len(name))
# # print(name.find("c"))
# # print(name.capitalize())
# # print(name.upper())
# # print(name.lower())
# # print(name.isdigit())
# # print(name.isalpha())
# # print(name.count("s"))
# # print(name.replace("s", "5"))
# # print(name * 4)



# x = 1
# y = 2.4
# z = "4"
# # x = float(x)
# # y = float(y)
# # z = float(z)
# print("X is " + str(x)) 
# print("Y is " + str(y)) 
# print("Z is " + str(z))


# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))
# print("Hello, " + name )
# print("You are " + str(age) + " years old and you are " + str(height) + " cm tall") 

# import math 
# pi = 3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(525))

# print(max(x, y, z))
# print(min(x, y, z))


# SLICING - Extracting a specific chunk or part from a list or string
#           indexing[] or slice[]
#           [start:stop:step]

# name = "Agostino Scholes"
# first_name = name[0:3]
# last_name = name[7:13]
# funky_name = name[0:8:2]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website = "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7, -4)
# print(website[slice])
# print(website2[slice])


# ESLE AND IF STATEMENTS - Used to decide to do something based on something being true or false
# age = int(input("How old are you?: "))
# if age == 100:
#     print("You are way too old") 
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You have not been born yet! ")
# else:
#     print("You are a child! ")


#LOGICAL OPERATORS (and, or, not) - Used to check if two or more conditional statements are true
# and - both conditions must be true
# temp = int(input("What is the temperature outside?: "))

# if temp >= 0 and temp <= 30:
#     print("The tempeerature is good today!")
#     print("Go outside!")
# elif temp < 0 or temp > 30:
#     print("The temperature is bad today!")
#     print("Stay inside!")


#While loops - A statement that will execute its block of code, as long as its condition remains true
name = None

while not name:
    name = input("Enter your name: ")
print("Hello " + name)
