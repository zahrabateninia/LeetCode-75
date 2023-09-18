""" Increasing Triplet Subsequence"""
'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that 
i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)

        if length >= 3:
            for i in range(length - 2):
                if nums[i] < nums[i + 1] and nums[i + 1] < nums[i + 2]:
                    return True
                    break
            else:
                return False
        else:
            return False
