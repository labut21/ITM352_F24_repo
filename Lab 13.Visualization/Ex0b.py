import matplotlib.pyplot as plt

x = list(range(0,10))
y = [e * 5 for e in x]

fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()