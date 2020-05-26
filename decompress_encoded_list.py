# https://leetcode.com/problems/decompress-run-length-encoded-list/
# We are given a list nums of integers representing a list compressed
# with run-length encoding.
# Consider each adjacent pair of elements [freq, val] = [nums[2*i],
# nums[2*i+1]] (with i >= 0).  For each such pair, there are freq
# elements with value val concatenated in a sublist. Concatenate all
# the sublists from left to right to generate the decompressed list.
# Return the decompressed list.

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        for idx, num in enumerate(nums):
            if idx & 1 == 0:
                for _ in range(num):
                    result.append(nums[idx + 1])

        return result

nums = [1, 2, 3, 4] # once 2 and three times 4 [2,4,4,4]
# nums = [1, 1, 2, 3] # once 1 and twice 3 [1,3,3]
# nums = [1, 5, 100, 9, 2, 2]

solution = Solution().decompressRLElist(nums)
print(solution)