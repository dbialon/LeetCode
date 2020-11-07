# https://leetcode.com/problems/hamming-distance/
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.
# Note: 0 <= x, y < 2**31


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = 0
        while x or y:
            if x & 1 != y & 1:
                d += 1
            x >>= 1
            y >>= 1
        return d

x, y = 255, 2

solution = Solution()
print(solution.hammingDistance(x, y))