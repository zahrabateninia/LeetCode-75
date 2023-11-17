"""
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.
"""


def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(length):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_length = right -left +1 - zero_count
            max_length = max(max_length, current_length)
        return max_length - 1 if max_length == length else max_length

            
        