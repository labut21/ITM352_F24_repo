def fahrenheit_to_celsius(fahrenheit):
  # Converts Fahrenheit to Celsius
  celsius = (fahrenheit - 32) * (5/9)
  return celsius

# Test the function
fahrenheit_temp = 32
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is equivalent to {celsius_temp}°C.")