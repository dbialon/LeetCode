# https://leetcode.com/problems/toeplitz-matrix/
# A matrix is Toeplitz if every diagonal from top-left to bottom-right
# has the same element.
# Now given an M x N matrix, return True if and only if the matrix is
# Toeplitz.

from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            if matrix[i-1][:-1] != matrix[i][1:]:
                return False
        return True


matrix = [[1,2,3,4],
          [5,1,2,3],
          [9,5,1,2]]

# matrix = [[1,2],[2,2]]

solution = Solution()
print(solution.isToeplitzMatrix(matrix))
