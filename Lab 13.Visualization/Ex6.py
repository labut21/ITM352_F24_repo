import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file_path = '/Users/lanceabut/Downloads/Trips from area 8.json'
with open(file_path, 'r') as file:
    data = json.load(file)

fares = [trip['fare'] for trip in data if 'fare' in trip]
trip_miles = [trip['trip_miles'] for trip in data if 'trip_miles' in trip]
dropoff_areas = [trip['dropoff_area'] for trip in data if 'dropoff_area' in trip]

# Make sure data is equal length
min_length = min(len(fares), len(trip_miles), len(dropoff_areas))
fares = fares[:min_length]
trip_miles = trip_miles[:min_length]
dropoff_areas = dropoff_areas[:min_length]

# Plot the data in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
scatter = ax.scatter(fares, trip_miles, dropoff_areas, c=fares, cmap='viridis', s=50)
ax.set_title("3D Plot of Fares, Trip Miles, and Dropoff Area")
ax.set_xlabel("Fare")
ax.set_ylabel("Trip Miles")
ax.set_zlabel("Dropoff Area")

# Adding color bar for reference
cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Fare')

plt.show()