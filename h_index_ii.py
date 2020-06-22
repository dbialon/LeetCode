# https://leetcode.com/problems/h-index-ii/

# Given an array of citations sorted in ascending order (each citation
# is a non-negative integer) of a researcher, write a function to
# compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has
# index h if h of his/her N papers have at least h citations each, and
# the other N − h papers have no more than h citations each."

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)

        for idx, _ in enumerate(citations):
            if citations[idx] >= length - idx:
                return length - idx

        return 0


# citations = [0,1,2,2,4,5,6]
citations = [11,15]

solution = Solution()
print(solution.hIndex(citations))