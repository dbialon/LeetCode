# https://leetcode.com/problems/three-consecutive-odds/
# Given an integer array arr, return true if there are three consecutive
# odd numbers in the array. Otherwise, return false. 

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr) - 2:
            if arr[i] & 1:
                if arr[i+1] & 1:
                    if arr[i+2] & 1:
                        return True
                    i += 1
                i += 1
            i += 1
        else:
            return False


# arr = [2,6,4,1]
arr = [1,2,34,3,4,5,7,23,12]


solution = Solution()
print(arr, solution.threeConsecutiveOdds(arr))
