# https://leetcode.com/problems/subsets/
# Given a set of distinct integers, nums, return all possible
# subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

from typing import List

class Solution:
    def combinations_generator(self, array: List[int], n: int):
        if n == 1:
            for item in array:
                yield [item]
        else:
            for idx, item in enumerate(array):
                for x in self.combinations_generator(array[idx+1:], n-1):
                    yield [item] + [i for i in x]


    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        indices = [n for n in range(len(nums))]
        k = 0
        for i in range(1, len(nums)+1):
            for idx in self.combinations_generator(indices, i):
                ans.append([])
                k += 1
                for j in idx:
                    ans[k].append(nums[j])

        return ans


array = [1,2,3]

solution = Solution()
print(solution.subsets(array))
