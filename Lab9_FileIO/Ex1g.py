import os

file_path = './names.txt'

# Check if the file exists and is readable
if os.path.exists(file_path) and os.access(file_path, os.R_OK):
    # Append a new name to the file
    with open(file_path, 'a') as names_file:  # Open in append mode
        names_file.write("Port, Dan\n")  # Add new name with newline

    # Print the entire contents of the file
    with open(file_path, 'r') as names_file:
        names = names_file.readlines()
    
    for name in names:
        print(name.strip())  # Print each name without extra whitespace
else:
    print(f"Error: The file '{file_path}' does not exist or is not readable.")