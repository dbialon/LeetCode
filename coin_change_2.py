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
    combinations = {0: 0}    
    def change(self, amount: int, coins: List[int]) -> int:

        for idx, coin in enumerate(coins):
            self.combinations[coin] = 1 + self.estimate_change(coin, coins[:idx])

        print(self.combinations)

        return self.estimate_change(amount, coins)

        
    def estimate_change(self, amount: int, coins: List[int]) -> int:
        if amount in self.combinations:
            return self.combinations[amount]
        
        if amount < 0:
            return 0

        result = 0
        for coin in coins:
            print(coin)
            result += self.estimate_change(amount - coin, coins)

        self.combinations[amount] = result

        return result


amount = 20
coins = [1, 2, 5]
# 52
# 511
# 2221
# 22111
# 211111
# 1111111

# amount = 3
# coins = [2]

# amount = 10
# coins = [10]

solution = Solution()
print(solution.change(amount, coins))
print(solution.combinations)