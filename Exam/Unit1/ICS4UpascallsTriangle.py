while True:
    maxline = int(input('Please inpute the number of lines you want to print:'))# ask the user for the number of lines
    if maxline > 0: # check if the input is valid
        break
    else:
        print ('Please input a number greater than 0')

# initialization the number and print the first line
print ('1')
line = 2
lines = [1]

# print the rest of the lines
for i in range(1, maxline): #loop to print 2 to maxline lines
    lines = [1] + [lines[j-1] + lines[j] for j in range(1, line - 1)] + [1] # calculate the numbers in now line
    for j in range(len(lines)): # print each number in the line
        print(lines[j], end=' ')
    print()
    line += 1 # shift to the next line

exit()