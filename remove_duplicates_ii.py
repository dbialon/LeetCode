# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.
# Do not allocate extra space for another array, you must do this
# by modifying the input array in-place with O(1) extra memory.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return len(nums)
        i, count = 0, 1
        for j in range(1, l):
            if nums[j] == nums[i]:
                count += 1
            else:
                if count == 1:
                    i += 1
                    nums[i] = nums[j]
                else:
                    nums[i+1] = nums[i]
                    i += 2
                    nums[i] = nums[j]
                    count = 1
        
        if count == 1:
            nums[i] = nums[j]
            return i + 1
        else:
            nums[i+1] = nums[j]
            return i + 2


nums = [0,0,0,0,0,0,1,2,2,2,2,2,3,3,4,4,4,4,5]

solution = Solution()
l = solution.removeDuplicates(nums)
print(nums[:l])
