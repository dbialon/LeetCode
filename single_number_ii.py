# https://leetcode.com/problems/single-number-ii/

# Given a non-empty array of integers, every element appears three times
# except for one, which appears exactly once. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you
# implement it without using extra memory?

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 3
            else:
                return nums[i-1]
        else:
            return nums[-1]


####################
### TESTING ONLY ###
####################

# TODO reduce runtime to linear time

# nums = [2,2,3,2]
nums = [0,1,0,1,0,1,99]

solution = Solution()
print(solution.singleNumber(nums))
