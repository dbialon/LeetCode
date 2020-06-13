# https://leetcode.com/problems/pascals-triangle/
#     [1]
#    [1,1]
#   [1,2,1]
#  [1,3,3,1]
# [1,4,6,4,1]
# Generate Pascal's triangle of a given height.

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [(n+1) * [1] for n in range(numRows)]

        for row in range(2, numRows):
            i = 1
            j = row - 1
            while i <= j:
                if i < j:
                    result[row][i] = result[row-1][i-1] + result[row-1][i]
                    result[row][j] = result[row-1][j-1] + result[row-1][j]
                else:
                    result[row][i] = result[row-1][i-1] + result[row-1][i]
                i += 1
                j -= 1
            
        for row in result:
            yield row


rows = 5

solution = Solution()
result = []
for row in solution.generate(rows):
    result.append(row)

print(result)
