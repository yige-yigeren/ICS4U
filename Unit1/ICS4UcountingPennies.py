import matplotlib.pyplot as plt
import numpy as np

radius = int(input("Enter the radius of the circle: "))
theta = np.linspace(0, 2*np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')

plots = 0
for i in range(-radius, radius+1, 1):
    for j in range(-radius, radius+1, 1):
        if i**2 + j**2 <= radius**2:
            plots += 1
            plt.scatter(i, j, color='green')
        else:
            plt.scatter(i, j, color='red')

print("The number of points in the circle is ", plots)

plt.show()