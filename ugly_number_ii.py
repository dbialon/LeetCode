# https://leetcode.com/problems/ugly-number-ii/
# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include
# 2, 3, 5.

class Solution:
    def __init__(self):
        self.uglies = [0 for _ in range(1691)]
        self.uglies[1] = 1
        idx2 = idx3 = idx5 = 1

        for i in range(2, 1691):
            L2 = self.uglies[idx2] * 2
            L3 = self.uglies[idx3] * 3
            L5 = self.uglies[idx5] * 5
            next_number = min(L2, L3, L5)
            self.uglies[i] = next_number
            if next_number == L2:
                idx2 += 1
            if next_number == L3:
                idx3 += 1
            if next_number == L5:
                idx5 += 1


    def nthUglyNumber(self, n: int) -> int:
        return self.uglies[n]
    

number = 137

solution = Solution()
print(solution.uglies)
print(solution.nthUglyNumber(number))
