import random
sum = 0
nums = []
for i in range(0,11):
    nums.append(random.randrange(0, 100))

print(nums)
nums.sort()
print(nums)

print("The biggest number in the list is", nums[10])
print("The smallest number in the list is", nums[0])
print("The number in the middle of the list is", nums[5])

for i in range(len(nums)):
    sum = sum + nums[i]
avg = sum/11
print("The average of the list is: ", avg)

if nums[i]>nums[i+1]:
    nums[i]=nums[i+1]

