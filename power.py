# https://leetcode.com/problems/powx-n/
# Implement pow(x, n), which calculates x raised to the power n (i.e. x^n).
# Constraints:
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return (x > 0) - (x < 0)
        elif n < 0:
            return self.power(1/x, -n)
        else:
            return self.power(x, n)

    
    def power(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n % 2 == 1:
            return x * self.power(x*x, n//2)
        else:
            return self.power(x*x, n//2)


x = 2.1
n = -3
# x = 0.00001
# n = 2147483647

solution = Solution()
print(solution.myPow(x, n))