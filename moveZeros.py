# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums: List[int]) -> None:
            # nums.sort(key=lambda x: x == 0) another solution 
            non_zero_idx = 0

            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i], nums[non_zero_idx] = nums[non_zero_idx], nums[i] # syntax of swap in python: a,b = b,a   :)
                    non_zero_idx += 1
