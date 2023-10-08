"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array. 
"""
# Approach
"""
The key idea is to use the dictionary num_count to keep track of the counts of each number. 
This way, we can efficiently check if a complementary number exists in 
the list for a given num that sums up to k. If it does, we perform an operation 
(increment count and decrement the count of the complementary number)
"""
def maxOperations(nums, k):
    count = 0 # maximum number of operations
    num_count = {} # stores the count of each number
    
    for num in nums:
        if k - num in num_count and num_count[k - num] > 0:
            count += 1
            num_count[k - num] -= 1
        else:
            num_count[num] = num_count.get(num, 0) + 1
    
    return count



nums = [1,2,3,4]
k=5
print(maxOperations(nums,k)) 
