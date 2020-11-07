# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
# Given an integer n and an integer array rounds. We have a circular
# track which consists of n sectors labeled from 1 to n. A marathon
# will be held on this track, the marathon consists of m rounds.
# The ith round starts at sector rounds[i - 1] and ends at sector
# rounds[i]. For example, round 1 starts at sector rounds[0] and ends
# at sector rounds[1]
# Return an array of the most visited sectors sorted in ascending order.
# Notice that you circulate the track in ascending order of sector numbers
# in the counter-clockwise direction (See the first example).

from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        count = {k:0 for k in range(1, n+1)}
        curr = rounds[0]
        count[curr] += 1
        for i in range(1, len(rounds)):
            while True:
                if curr == rounds[i]:
                    break
                elif curr == n:
                    curr = 1
                else:
                    curr += 1
                count[curr] += 1

        max_c = max(count.values())
        ans  = [k for k in count if count[k] == max_c]
        return ans


n = 7
rounds = [4,6,1,5,2]

solution = Solution()
print(solution.mostVisited(n, rounds))
