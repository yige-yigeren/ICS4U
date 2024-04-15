num=1
while num < 500:
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num)
    num += 1
exit(0)