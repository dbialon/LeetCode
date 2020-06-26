# https://leetcode.com/problems/merge-sorted-array/
# Given two sorted integer arrays nums1 and nums2,
# merge nums2 into nums1 as one sorted array.
# Note:
# The number of elements initialized in nums1 and nums2 are m and n
# respectively. You may assume that nums1 has enough space (size
# that is greater or equal to m + n) to hold additional elements
# from nums2.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        n -= 1
        m -= 1
        while n > -1 and m > -1:
            if nums1[m] > nums2[n]:
                nums1[m+n+1] = nums1[m]
                nums1[m] == 0
                m -= 1
            else:
                nums1[m+n+1] = nums2[n]
                n -= 1
        while n > -1:
            nums1[n] = nums2[n]
            n -= 1

nums1 = [1,3,5,0,0,0]
m = 3
nums2 = [1,3,5]
n = 3

print(nums1, nums2)
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)
