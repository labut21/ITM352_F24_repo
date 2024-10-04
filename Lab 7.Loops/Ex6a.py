my_tuple = (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989)


# Attempt to append a new element to the tuple
try:
   my_tuple.append(1990)
except AttributeError as e:
   print(f"Error: {e}")