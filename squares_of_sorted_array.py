# https://leetcode.com/problems/squares-of-a-sorted-array/
# Given an array of integers A sorted in non-decreasing order,
# return an array of the squares of each number, also in sorted
# non-decreasing order.

from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x * x for x in A)


A = [-4,-1,0,3,10]
# A = [-7,-3,2,3,11]
# A = [-1,0,0,0]
# A = [-3,-3,-2,1]
# A = [-1,0,1,1,11]
print(A)

solution = Solution()
print(solution.sortedSquares(A))
