def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b-1)