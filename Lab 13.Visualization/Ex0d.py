import matplotlib.pyplot as plt

x = list(range(0,10))
y1 = [e * 5 for e in x]
y2 = [e * e for e in x]

fig, ax = plt.subplots() # Create a figure containing a single Axas
ax.plot(x,y1) # Plot some data on the Axes
ax.scatter(x,y1)
ax.plot(x,y2)
ax.scatter(x,y2)
plt.show()