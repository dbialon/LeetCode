# https://leetcode.com/problems/monotonic-array/
# An array is monotonic if it is either monotone increasing
# or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j]. 
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return true if and only if the given array A is monotonic.

from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[0] == A[-1]:
            for i in range(len(A) - 1):
                if A[i] != A[i+1]:
                    return False
            else:
                return True
        elif A[0] < A[-1]:
            for i in range(len(A) - 1):
                if A[i] > A[i+1]:
                    return False
            else:
                return True
        else:
            for i in range(len(A) - 1):
                if A[i] < A[i+1]:
                    return False
            else:
                return True


arrays = [[1,2,2,3],
          [6,5,4,4],
          [1,3,2],
          [1,2,4,5],
          [1,1,1]]

solution = Solution()
for array in arrays:
    print(solution.isMonotonic(array))
