# Ask user for birth year 
year_entered = input("Please enter the year you were born (four-digit number): ") 

# Convert the year to integer 
birth_year = int(year_entered) 

# Get current year 
current_year = 2024 

# Subtract current year from birth year entered
age = current_year - birth_year 

# Print user birth year
print(f"You entered: ", birth_year)

# Print calculated age 
print(f"Your age is: {age}")