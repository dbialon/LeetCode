# https://leetcode.com/problems/add-digits/
# Given a non-negative integer num, repeatedly add all its digits until
# the result has only one digit.

class Solution:
    def addDigits1(self, num: int) -> int:
        while num > 9:
            sum_n = 0
            for digit in str(num):
                sum_n += int(digit)
            num = sum_n
        
        return num


    def addDigits2(self, num: int) -> int:
        if num < 10:
            return num
        num %= 9
        if num == 0:
            return 9
        else:
            return num


solution = Solution()
for n in range(24, 35):
    print(n, solution.addDigits2(n))
