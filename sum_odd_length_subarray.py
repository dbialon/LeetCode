# https://leetcode.com/problems/sum-of-all-odd-length-subarrays
# Given an array of positive integers arr, calculate the sum
# of all possible odd-length subarrays.
# A subarray is a contiguous subsequence of the array.
# Return the sum of all odd-length subarrays of arr.

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        n = 0
        for i in range(l):
            for j in range(i+1, l+1):
                if len(arr[i:j]) % 2 == 1:
                    n += sum(arr[i:j])
                    
        return n

# arr = [1,4,2,5,3]
# arr = [1,2]
arr = [10,11,12]

solution = Solution()
print(solution.sumOddLengthSubarrays(arr))
