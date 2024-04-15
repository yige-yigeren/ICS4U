
# Date: 2024/04/15
# Course: ICS4U

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

points = radius * 4 + 1 # the number of points on axis in the circle 
for i in range(1, radius+1, 1): # loop through the all point in the square
    for j in range(1, radius+1, 1):
        if pointoncircle(i, j, radius): # check if the point is in the circle
            points += 4 # increment the number of points in the circle
print("The number of points in the circle is ", points) 

exit()