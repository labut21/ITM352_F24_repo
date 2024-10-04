# Get whole number
number_entered = input("enter a whole number betweeen 1 and 100: ")

# Convert the number to integer and square it
number_squared = int(number_entered)**2

# Print the number and square it
print("The number you entered is: " + number_entered + "\nThe square of the number you entered is: " + str(number_squared))

# One alternative way to print the result message
number = int(input("Enter a whole number between 1 and 100"))
print(f"The square of "+ str(number) + " is " + str(number ** 2) )