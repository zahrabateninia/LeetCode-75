""" Increasing Triplet Subsequence"""
'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that 
i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)

        if length >= 3:
            smallest = float('inf')
            second_smallest = float('inf')
            
            for num in nums:
                if num <= smallest:
                    smallest = num
                elif num <= second_smallest:
                    second_smallest = num
                else:
                    return True
                    break
            else:
                return False
        else:
            return False