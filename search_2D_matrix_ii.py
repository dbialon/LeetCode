# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Write an efficient algorithm that searches for a value in
# an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        i = 0
        while i < len(matrix[0]):
            if matrix[0][i] == target:
                return True
            elif matrix[0][i] > target:
                if i > 0:
                    return self.searchMatrix([cols[:i] for cols in matrix[1:]], target)
                else:
                    return False
            else:
                i += 1

        j = 1
        while j < len(matrix):
            if matrix[j][0] == target:
                return True
            elif matrix[j][0] > target:
                if j > 0:
                    return self.searchMatrix(matrix[1:j], target)
                else:
                    return False
            else:
                j += 1

        return self.searchMatrix([cols[1:] for cols in matrix[1:]], target)


# matrix = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# matrix = [[0],[1],[3],[4],[5]]
matrix = [[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]]
target = 15

solution = Solution()
print(solution.searchMatrix(matrix, target))
