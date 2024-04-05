import random
nums = []
# Add 75 numbers to the list
for i in range(75):
    nums.append(random.randint(15,50))
print(nums)

print("Please choose a number to count")
num = int(input())
count = 0
for i in range(75):
    if nums[i] == num:
        count += 1
print("The number",num,"appears",count,"times in the list")
exit(0)