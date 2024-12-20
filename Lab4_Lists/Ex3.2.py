first_name = input("First name: ")
middle_name = input("Middle name: ")
last_name = input("Last name: ")

# Ex1a
full_name = first_name + " " + middle_name[0] + ". " + last_name

# Ex1b
full_name = f"{first_name} {middle_name[0]}. {last_name}"

#Ex1c
full_name = "%s %s. %s"%(first_name, middle_name[0], last_name)

#Ex1d
full_name = "{} {}. {}".format(first_name, middle_name[0], last_name)

#Ex1e 
full_name = "".join([first_name," ", middle_name[0],". ",last_name])

#Ex1f
# List the inputs for storing it
name_parts = [first_name, middle_name[0], last_name]

full_name = "{} {}. {}".format(*name_parts)

print(full_name)