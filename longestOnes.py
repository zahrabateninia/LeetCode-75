'''
Given a binary array nums and an integer k, return the maximum number 
of consecutive 1's in the array if you can flip at most k 0's.
'''

def longestOnes(nums, k: int) -> int:
    l = r = 0  # Initialize left and right pointers
    
    for r in range(len(nums)):  # Iterate through the array using the right pointer
        if nums[r] == 0:  # If the current element is 0
            k -= 1  # Decrement k (as we're flipping a 0 to 1)
        
        if k < 0:  # If k becomes negative, we've used up all flips
            if nums[l] == 0:  # If the leftmost element was a 0
                k += 1  # Increment k (as we're flipping it back to 0)
            l += 1  # Move the left pointer one step to the right
    
    return r - l + 1  # Calculate the length of the longest subarray with at most k flips
     