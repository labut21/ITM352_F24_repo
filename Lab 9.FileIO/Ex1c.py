with open('./names.txt','r') as names_file:
    names = names_file.read()
lines = names.split('\n')
print(f"{names}\nThere are {len(lines)} names")