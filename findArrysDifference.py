# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

def findDifference(nums1, nums2):
        answer1 = []
        answer2 = []
        for num in nums1:
            if num not in nums2:
                answer1.append(num)
        for num in nums2:
            if num not in nums1:
                answer2.append(num)
        return [set(answer1), set(answer2)]