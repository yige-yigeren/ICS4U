print("Calculate the value of a^b")
print("Please enter the value of a")
a = int(input())
print("Please enter the value of b")
b = int(input())

while b < 0:
    print("Please enter a positive value of b")
    b = int(input())
if b == 0:
    print("The value of a^b is 1")
    exit(0)

temp = a
while b > 1:
    a *= temp
    b -= 1
print("The value of a^b is",a)
exit(0)