# https://leetcode.com/problems/count-number-of-teams/
# There are n soldiers standing in a line. Each soldier is assigned
# a unique rating value.
# You have to form a team of 3 soldiers amongst them under the following rules:
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if:
# (rating[i] < rating[j] < rating[k])
# or
# (rating[i] > rating[j] > rating[k])
# where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions
# (soldiers can be part of multiple teams).

from typing import List

class Solution:
    def is_valid_team(self, arr: List[int]) -> bool:
        if arr[0] > arr[1] > arr[2]:
            return True
        if arr[0] < arr[1] < arr[2]:
            return True
        return False


    def combinations(self, arr: List[int], n: int) -> List[List[int]]:
        if n == 1:
            for item in arr:
                yield item
        else:
            for idx, item in enumerate(arr):
                for x in self.combinations(arr[idx+1:], n-1):
                    if isinstance(x, int):
                        yield [item] + [x]
                    else:
                        yield [item] + x


    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0

        teams = self.combinations(rating, 3)
        
        ans = 0
        
        for team in teams:
            if self.is_valid_team(team):
                ans += 1

        return ans


ratings = [2,5,3,4,1]

solution = Solution()
print(solution.numTeams(ratings))
