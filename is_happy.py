# https://leetcode.com/problems/happy-number/
# Write an algorithm to determine if a number n is "happy".
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum
# of the squares of its digits, and repeat the process until the number
# equals 1 (where it will stay), or it loops endlessly in a cycle which
# does not include 1. Those numbers for which this process ends in 1 
# are happy numbers.
# Return True if n is a happy number, and False if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        while True:
            powers = 0
            while n != 0:
                powers += (n % 10) ** 2
                n //= 10
            if powers == 1:
                return True
            else:
                if powers in results:
                    return False
                else:
                    results.add(powers)
                    n = powers


solution = Solution()
for n in range(1, 100):
    print(n, "is happy:", solution.isHappy(n))