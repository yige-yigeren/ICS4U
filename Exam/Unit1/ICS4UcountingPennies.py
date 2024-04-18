# import the necessary libraries
import matplotlib.pyplot as plt # draw
import numpy as np # math

# the function pointoncircle is to determine if a point is on the circle
def pointoncircle(x, y, radius):
    if x**2 + y**2 <= radius**2:
        return True
    else:
        return False

# ask the user for the radius of the circle
while True:
    radius = int(input("Enter the radius of the circle: "))
    if radius > 0:
        break
    else:
        print ('Please input a number greater than 0')

# create the circle
theta = np.linspace(0, 2*np.pi, 100) # make the points to draw the circle
x = radius * np.cos(theta)
y = radius * np.sin(theta)
plt.plot(x, y) # draw the circle
# create axis
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.gca().set_aspect('equal', adjustable='box') # set the show

points = 0 # initialize the number of points in the circle
for i in range(-radius, radius+1, 1): # loop through the all point in the square
    for j in range(-radius, radius+1, 1):
        if pointoncircle(i, j, radius): # check if the point is in the circle
            plt.scatter(i, j, color='green') # draw the point in the circle
            points += 1 # increment the number of points in the circle
print("The number of points in the circle is ", points) 
plt.show() #show the plot
exit()