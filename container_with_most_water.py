# https://leetcode.com/problems/container-with-most-water/
# Given n non-negative integers a1, a2, ..., an, where each
# represents a point at coordinate (i, ai). n vertical lines
# are drawn such that the two endpoints of line i is at (i, ai)
# and (i, 0). Find two lines, which together with x-axis forms
# a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] > height[right]:
                current = right - 1
                while height[current] < height[right] and current > 0:
                    current -= 1
                right = current
            elif height[right] > height[left]:
                current = left + 1
                while height[current] < height[left] and current < len(height):
                    current += 1
                left = current
            else:
                left += 1
                right -= 1

        return ans


container = [1,8,6,2,5,4,8,3,7]

solution = Solution()
print(solution.maxArea(container))
