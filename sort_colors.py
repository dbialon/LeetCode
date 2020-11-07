# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/
# 540/week-2-june-8th-june-14th/3357/

# Given an array with n objects colored red, white or blue, sort them
# in-place so that objects of the same color are adjacent, with
# the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color
# red, white, and blue respectively.
# Note: You are not supposed to use the library's sort function for
# this problem.

from typing import List
from time import sleep

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_0 = 0
        count_1 = 0

        for item in nums:
            if item == 0:
                count_0 += 1
            elif item == 1:
                count_1 += 1

        for idx, _ in enumerate(nums):
            if count_0 > 0:
                nums[idx] = 0
                count_0 -= 1
            elif count_1 > 0:
                nums[idx] = 1
                count_1 -= 1
            else:
                nums[idx] = 2

        # last_1 = 0
        # first_2 = len(nums) - 1

        # for idx in range(first_2):  # first_2 is initially equal to len(nums) - 1
        #     while nums[idx] != min(nums):
        #         if nums[idx] == 2:
        #             nums[idx], nums[first_2] = nums[first_2], nums[idx]
        #             first_2 -= 1
        #         elif nums[idx] == 1: ## TODO
        #             ## for some cases if works
        #             ## for others elif works
        #             if last_1 == 0:
        #                 last_1 = idx + 1
        #             nums[idx], nums[last_1] = nums[last_1], nums[idx]
        #             last_1 += 1
        #         if first_2 - last_1 <= 2:
        #             return None


# nums = [2,0,2,1,1,0]
# nums = [2,0,2,2,2,1,2,1,2,1,2,1,0,1,1,1,0]
nums = [1, 2]
print(nums, len(nums))

solution = Solution()
solution.sortColors(nums)

print(nums, len(nums))