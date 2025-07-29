'''
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''
# result[i] = multiply of all left * multiply of all right
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]
        
        return products