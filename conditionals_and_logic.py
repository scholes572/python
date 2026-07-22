# ELSE AND IF STATEMENTS - Used to decide to do something based on something being true or false
age = int(input("How old are you?: "))
if age == 100:
    print("You are way too old") 
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You have not been born yet! ")
else:
    print("You are a child! ")


# LOGICAL OPERATORS (and, or, not) - Used to check if two or more conditional statements are true
# and - both conditions must be true
temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The tempeerature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")