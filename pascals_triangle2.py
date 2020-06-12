# https://leetcode.com/problems/pascals-triangle-ii/
# [1,4,6,4,1], k = 4
# Generate k-th row of Pascal's triangle where 0 <= k <= 33.

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 or rowIndex == 1:
            return (rowIndex+1) * [1]

        result = [1, 1]
        for row in range(2, rowIndex+1):
            i = 1
            while i < row:
                if i <= row // 2:
                    result[row-i] = result[i] + result[i-1]
                else:
                    result[row-i] = result[i]
                i += 1
            result.append(1)

        return result

rows = range(7)

solution = Solution()
for row in rows:
    print(solution.getRow(row))
