print("Please type the function like this: ax^2 + bx + c")
print("Now, please enter the values of a")
a = int(input())
print("Now, please enter the values of b")
b = int(input())
print("Now, please enter the values of c")
c = int(input())
print("The quadratic formula is:")
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print("x1 =", x1,"; x2 =", x2)
elif d == 0:
    x = -b / (2*a)
    print("x =", x)
else:
    print("This equation has no real roots")
exit(0)