# https://leetcode.com/problems/ugly-number/
# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include
# 2, 3, 5.
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−231,  231 − 1].


class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1 or num > 2**31 - 1:
            return False
        while num != 1:
            if num % 2 == 0:
                num //= 2
            elif num % 3 == 0:
                num //= 3
            elif num % 5 == 0:
                num //= 5
            else:
                return False
        return True


solution = Solution()
for number in range(30):
    print(number, solution.isUgly(number))
