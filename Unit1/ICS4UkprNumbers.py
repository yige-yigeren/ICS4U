numrange = 20
pnums = []
for i in range(2,numrange):
    prime = True
    for j in range(2,i//2+1):
        if i % j == 0:
            prime = False
            break
    if prime:
        pnums.append(i)
num = 1
while num <= numrange:
    temp = 1 # number of KPR numbers
    npnum = 0 # number of prime number
    while pnums[npnum] <= num:
        ptemp = pnums[npnum] # prime number power
        lptemp = ptemp
        while ptemp <= num:
            lptemp = ptemp # last prime number power
            ptemp = ptemp * pnums[npnum] # prime number power
        temp = temp * lptemp
        if npnum < len(pnums) - 1:
            npnum += 1
        else:
            break
    print (num, " KPR number is ", temp)
    num += 1
exit(0)