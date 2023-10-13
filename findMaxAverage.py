"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

def findMaxAverage(nums, k: int) -> float:

        start_idx = 0
        end_idx = k-1
        max_sum = float('-inf')  # Initialize max_sum with negative infinity
        length = len(nums)
        window_sum = sum(nums[start_idx:end_idx+1])  # Calculate sum of first window

        while end_idx < length - 1:
            max_sum = max(max_sum, window_sum)  # Update max_sum if necessary
            window_sum += nums[end_idx+1] - nums[start_idx]  # Update window_sum
            start_idx += 1
            end_idx += 1

        max_sum = max(max_sum, window_sum)  # Check max_sum one last time
        return max_sum / k

