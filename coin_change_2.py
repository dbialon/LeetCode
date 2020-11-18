# https://leetcode.com/explore/challenge/card/
# june-leetcoding-challenge/539/week-1-june-1st-june-7th/3353/

# You are given coins of different denominations and a total amount
# of money. Write a function to compute the number of combinations
# that make up that amount. You may assume that you have infinite
# number of each kind of coin.

# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Example 3:
# Input: amount = 10, coins = [10] 
# Output: 1

from typing import List


class Solution:

    def __init__(self):
        self.combinations = {0: 1}

    def change(self, amount: int, coins: List[int]) -> int:

        for i in range(1, amount+1):
            self.combinations[i] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                self.combinations[i] += self.combinations[i-coin]

        return self.combinations[amount]


amount = 29
coins = [1, 2, 5]

# amount = 3
# coins = [2]

# amount = 10
# coins = [10]

solution = Solution()
print(solution.change(amount, coins))
