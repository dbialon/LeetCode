# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# We have an array A of integers, and an array queries of queries.
# For the i-th query val = queries[i][0], index = queries[i][1],
# we add val to A[index].  Then, the answer to the i-th query is
# the sum of the even values of A.
# (Here, the given index = queries[i][1] is a 0-based index,
# and each query permanently modifies the array A.)
# Return the answer to all queries.  Your answer array
# should have answer[i] as the answer to the i-th query.

from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        answer = [0 for _ in range(len(queries))]

        for idx, query in enumerate(queries):
            A[query[1]] += query[0]
            for number in A:
                if number & 1 == 0:
                    answer[idx] += number

        return answer


####################
### TESTING ONLY ###
####################

# Input: 
A = [1,2,3,4]
queries = [[1,0], [-3,1], [-4,0], [2,3]]
# Output: [8,6,2,4]

solution = Solution().sumEvenAfterQueries(A, queries)
print(solution)