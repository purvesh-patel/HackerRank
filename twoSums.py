nums = [10,20,30,40,50,60,70,80,90,100]
target = 110

print(nums, target)
print(" ")

# for i in nums:
#     print(i)


print(type(nums), len(nums), nums[0], print(target))

# for j in (0,len(nums)):
#     print(j)

for i in range(len(nums)):
    if (i + 1) < len(nums):
        #print(nums[i], nums[i + 1])
        if (nums[i] + nums[i+1]) == target:
            print(nums[i], nums[i + 1])
            print(i, i+1)
