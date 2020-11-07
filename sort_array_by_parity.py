# https://leetcode.com/problems/sort-array-by-parity/
# Given an array A of non-negative integers, return an array consisting
# of all the even elements of A, followed by all the odd elements of A.
#  You may return any answer array that satisfies this condition.

from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        
        while i < j:
            if A[i] & 1 == 1 and A[j] & 1 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            if A[j] & 1 == 1:
                j -= 1
            if A[i] & 1 == 0:
                i += 1
                
        return A


A = [4,1,3,7,2,8,6,9]

solution = Solution()
print(solution.sortArrayByParity(A))
