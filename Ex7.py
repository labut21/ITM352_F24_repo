# Get Fahrenheit temperature
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * (5/9)

# Print the temperature in Fahrenheit and the equivalent temperature in Celsius
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")