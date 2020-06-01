# https://leetcode.com/problems/transpose-matrix/
# Given a matrix A, return the transpose of A.
# The transpose of a matrix is the matrix flipped over its
# main diagonal, switching the row and column indices of the matrix.
# 123     147
# 456 --> 258
# 789     369

from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = []
        i, n = 0, len(A[0])

        while i < n:
            B.append([])
            for idx, _ in enumerate(A):
                B[i].append(A[idx][i])
            i += 1

        return B


####################
### TESTING ONLY ###
####################

A = [[1,2,3],[4,5,6],[7,8,9]]
# A = [[1,2,3],[4,5,6]]
# A = [[1,2,3]]
# A = [[1]]

print("A:", A)
solution = Solution().transpose(A)
print("B:", solution)