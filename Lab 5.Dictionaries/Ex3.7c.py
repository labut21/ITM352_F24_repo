# Define the list of taxi trip durations in miles
miles = [1.1, 0.8, 2.5, 2.6]

# Define the tuple of fares for the same number of trips
fares = ("$6.25", "$5.25", "$10.50", "$8.05")

# Create a dictionary using zip() and dict()
trip_dict = dict(zip(miles, fares))

# Print the entire dictionary
print(trip_dict)

# Print the duration and cost of the 3rd trip
third_trip_duration = miles[2]
third_trip_fare = trip_dict[third_trip_duration]
print(f"The 3rd trip was: {third_trip_duration} miles, Cost: {third_trip_fare}")