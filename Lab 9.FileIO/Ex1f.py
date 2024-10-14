import os

file_path = './names.txt_bad'  # Change to a non-existing file

try:
    # Check if the file exists and is readable
    if os.path.exists(file_path) and os.access(file_path, os.R_OK):
        with open(file_path, 'r') as names_file:
            names = names_file.readlines()
        
        # Remove newline characters and count names
        num_names = len(names)
        for name in names:
            print(name.strip())  # Strip whitespace and print each name

        print(f"There are {num_names} names")
    else:
        print(f"Error: The file '{file_path}' does not exist or is not readable.")
except Exception as e:
    print(f"An error occurred: {e}")