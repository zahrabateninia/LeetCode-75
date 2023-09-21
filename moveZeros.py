# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

nums = [0,3,12,0,3] # [3,12,3,0,0]
zeros=[]

for num in nums:
    if num == 0:
        zeros.append(num)
        nums.remove(num)

nums.extend(zeros)
print(nums)