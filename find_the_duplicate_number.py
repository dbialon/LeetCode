# https://leetcode.com/problems/find-the-duplicate-number/
# Given an array nums containing n + 1 integers where each integer
# is between 1 and n (inclusive), prove that at least one duplicate
# number must exist. Assume that there is only one duplicate number,
# find the duplicate one.
# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be
# repeated more than once.

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                if nums[i] == nums[j]:
                    return nums[i]


nums = [2,3,3,1,4]

solution = Solution()
print(solution.findDuplicate(nums))