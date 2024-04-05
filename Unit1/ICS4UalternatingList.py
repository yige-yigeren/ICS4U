import random
nums = []
length = random.randrange(4,20,2)
while len(nums) < length:
    nums.append(random.randint(0,100))
print("The original list is",nums)
newnums = []
lengthnew = 0
while len(newnums) < length:
    newnums.append(nums[lengthnew])
    newnums.append(nums[length-lengthnew-1])
    lengthnew += 1
print("The new list is",newnums)