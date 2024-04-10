#Open the file for reading
file = open("data.txt","r")

#Make an empty list to store the data
x = []

#Read the 10 lines of the file and append to the list
for i in range(0,10):
	x.append(file.readline())

#Done reading so close the file
file.close()

#Print the results of the read to the screen
print(x)