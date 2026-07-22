#While loops - A statement that will execute its block of code, as long as its condition remains true
count = 1
while count <= 3:
    print(f"Loop running: {count}")
    count += 1
print("Loop finished")

total = 0 #Starts with a 0 because nothing is in the sum yet.
user_input = -1

while user_input != 0:
    user_input = int(input("Enter a number to add then if you want the total, Press 0 to stop: "))
    total += user_input
print(f"The total sum is : {total}")

