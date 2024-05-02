def f(x): # calculate the value of the polynomial at x
    return sum([coefs[i] * x ** i for i in range(len(coefs))])

def df(x): # calculate the value of the polynomial at x
    return (sum([coefs[i+0.0001] * x ** i for i in range(len(coefs))]) - sum([coefs[i] * x ** i for i in range(len(coefs))]))/0.0001

def adf(x): # calculate the derivative of the polynomial at x
    return sum([i * coefs[i] * x ** (i - 1) for i in range(1, len(coefs))])

max_power = int(input("Enter the maximum power of the polynomial: "))
coefs = []
for i in range(max_power + 1):
    coefs.append(float(input("Enter the coefficient of x^" + str(i) + ": ")))
x0 = int(input("Enter the initial guess: "))
max_iter = int(input("Enter the maximum number of iterations: "))
tol = float(input("Enter the tolerance: "))

while True:
    x1 = x0 - f(x0) / df(x0)
    if abs(x1 - x0) < tol: # check if the difference between x1 and x0 is less than the tolerance
        print("The root is", x1)
        exit()
    elif max_iter == 0: # check if the maximum number of iterations has been reached
        print("Failed to converge.")
        exit()
    x0 = x1
    max_iter -= 1
    print(f'F({x1}):{f(x1)}')