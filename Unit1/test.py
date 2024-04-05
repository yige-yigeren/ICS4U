#Finding KPR Numbers (aka Fractorials)
def KPR(n):
    f = n

    while True:

        #Count down loop from n so it breaks faster if not found
        for i in range(n, 0, -1):

            #Break if not a factor
            if f % i == 0:
                found = True
            else:
                found = False
                break
        if found:
            return f
        else:
            f = f + n # Only need to check multiples of n to make faster


# Main Program
for i in range(1, 21):
    print(i,": ", KPR(i))