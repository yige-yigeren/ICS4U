import math

print("Please type a integer")
a = int(input())
while a != 1:
    if a % 2 == 0:
        a = a/2
    else:
        a = 3*a + 1
    print(a)
exit(0)