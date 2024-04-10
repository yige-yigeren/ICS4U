cases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
disabled = input().split(',')
for i in range(len(disabled)):
    cases[int(disabled[i])-1] = 0
sum = 0
for i in range(len(cases)):
    sum = sum + cases[i]
average = sum / len(cases)
post = int(input())
if post > average:
    print("Deal")
else:
    print("No Deal")