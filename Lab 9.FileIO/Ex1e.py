with open('./names.txt', 'r') as names_file:
    names = names_file.readlines()  # Read all lines into a list

# Remove newline characters and count names
num_names = len(names)
for name in names:
    print(name.strip())  # Strip whitespace and print each name

print(f"There are {num_names} names")