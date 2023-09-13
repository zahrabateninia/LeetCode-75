'''
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''

nums = [1,2,3,4]
answer=[] 
i = 0

while i < len(nums): #i =0
    popped_item = nums.pop(i) # popped_item = 1
    result_of_multiply = 1
    for num in nums: # num = 2 first num 
        result_of_multiply *= num # 2 then 6 and then 24 so result is 24 

    answer.append(result_of_multiply)# answer = [24]
    nums.insert(i, popped_item)  # nums is again the same as before the while loop
    i += 1
print(answer)
