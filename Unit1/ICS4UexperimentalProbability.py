import random
def coin():
    return random.randint(0, 1)

def dice():
    return random.randint(1, 6)

times = random.randint(100, 1000)
success = 0
for range in range(1, times):
    if coin() == 1:
        if dice()%2 == 0:
            # 判断是否为奇数
            if dice()%2 == 1:
                if dice() <=4 & dice() >=2:
                    success += 1

print("Times: ", times, " Success: ", success)
print("Experimental probability is ", success/times)