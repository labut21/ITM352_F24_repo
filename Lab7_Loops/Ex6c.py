my_tuple = (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989)


# Append a new element to the tuple
try:
   my_tuple.append(1990)
except AttributeError:
   print("Error: You attempted to append a value to a tuple.")