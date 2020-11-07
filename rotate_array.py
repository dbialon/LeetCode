# https://leetcode.com/problems/rotate-array/
# Given an array, rotate the array to the right by k steps,
# where k is non-negative.
# Follow up:
# Try to come up as many solutions as you can, there are at least
# 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def swap(a, b):
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1


        length = len(nums)
        k %= length

        # reverse the order of the first len(nums)-k elements
        i, j = 0, length - k - 1
        swap(i, j)

        # reverse the order of the last k elements
        i, j = length - k, length - 1
        swap(i, j)

        # reverse the whole array
        i, j = 0, length - 1
        swap(i, j)


nums = [1,2,3,4,5,6,7]
k = 8

print(nums)
solution = Solution()
solution.rotate(nums, k)
print(nums)
