# https://leetcode.com/problems/search-a-2d-matrix/
# Write an efficient algorithm that searches for a value in
# an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer
# of the previous row.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break
                j += 1
            i += 1

        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 30

solution = Solution()
print(solution.searchMatrix(matrix, target))
