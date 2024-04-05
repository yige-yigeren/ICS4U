# caculate prime numbers from 1 to 50
pnums = []
for i in range(1,50):
    prime = True
    for j in range(2,i):
        if i % j == 0:
            prime = False
            break
    if prime:
        pnums.append(i)

# caculate KPR numbers from 1 to 50
num = 1
while num <= 50:
    temp = 0 # number of KPR numbers
    npnum = 0 # number of prime number
    while pnums[npnum] < num:
        ptemp = pnums[npnum] # prime number power
        while ptemp < num:
            lptemp = ptemp # last prime number power
            ptemp * pnums[npnum] # prime number power
        temp * lptemp
    print (num, " KPR number is ", temp)
    num += 1

        