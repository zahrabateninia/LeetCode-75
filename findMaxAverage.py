"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""


def findMaxAverage(nums, k: int) -> float:
            
    start_idx = 0
    end_idx = k-1
    max_sum = 0
    length = len(nums)
    window_sum = 0
    # first window
    for i in range(start_idx, end_idx+1):
        window_sum += i 
    num_of_window = length - k
    
    if max_sum < window_sum:
        max_sum = window_sum
    return max_sum/ k



nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))