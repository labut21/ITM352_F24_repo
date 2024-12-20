# Ask user for a number using stdin
number = float(input("Enter a decimal formatted number between 1 and 10: "))

# Round the values to two decimal places
square_num = round(number ** 2, 2)

# Print out the square of the input
print(f"The square of "+ str(number) + " is " + str(square_num) )