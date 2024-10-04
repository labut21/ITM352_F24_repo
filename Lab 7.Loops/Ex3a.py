myTuple = ('hello', 10, 'goodbye', 3, 'goodnight', 5)


strCount = 0
for elt in myTuple:
# Count how many of the elements are strings
   if isinstance(elt,str):
       strCount = strCount + 1
print(f"There are {strCount} strings in myTuple")