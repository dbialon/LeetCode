# https://leetcode.com/problems/search-insert-position/

# Given a sorted array and a target value, return the index
# if the target is found. If not, return the index where
# it would be if it were inserted in order.
# You may assume no duplicates in the array.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        idx = 0
        for num in nums:
            if num >= target:
                return idx
            idx += 1


array = [1, 3, 5, 6]
number = 7

solution = Solution()
print(solution.searchInsert(array, number))