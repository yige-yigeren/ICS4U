import time
import random
num = random.randint(1000000, 1000000000)
print(num)
def doThis(x):

    if x == 0:
        return 0
    else:
        return x % 10 + doThis(x // 10)

start_time = time.perf_counter()

print(doThis(num))

end_time = time.perf_counter()
elapsed_time1 = end_time - start_time

print("recursive", (elapsed_time1 * 1000), "seconds" )

start_time = time.perf_counter()
dothis = 0
for i in str(num):
    dothis = dothis + num%10
    num = num//10
print(dothis)
end_time = time.perf_counter()
elapsed_time2 = end_time - start_time

print("iterative", (elapsed_time2 * 1000), "seconds" )

print("The recursive function is", elapsed_time1/elapsed_time2, "times faster than the iterative function")
