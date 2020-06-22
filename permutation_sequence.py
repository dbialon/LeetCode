# https://leetcode.com/problems/permutation-sequence/

# The set [1,2,3,...,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get
# the following sequence for n = 3:
#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"
# Given n and k, return the kth permutation sequence.
# Note:
# * Given n will be between 1 and 9 inclusive.
# * Given k will be between 1 and n! inclusive.

import itertools

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        input_string = "123456789"[:n]
        i = 1
        for permutation in itertools.permutations(input_string):
            if i == k:
                return ''.join(permutation)
            i += 1

    def permutations(self, string: str, i: int) -> None:
        if i == 1:
            for letter in string:
                yield letter
        else:
            for idx, letter in enumerate(string):
                for char in self.permutations(string[:idx] + string[idx+1:], i-1):
                    yield letter + char

    def get_permutation(self, n: int, k: int) -> str:
        input_string = "123456789"[:n]
        for idx, permutation in enumerate(self.permutations(input_string, n), 1):
            if idx == k:
                return permutation


solution = Solution()
print(solution.get_permutation(8, 33_333))
print(solution.getPermutation(8, 33_333))