# https://leetcode.com/problems/string-compression/
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller
# than or equal to the original array.
# Every element of the array should be a character (not int)
# of length 1.
# After you are done modifying the input array in-place,
# return the new length of the array.
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cursor = 0
        count = 0

        for idx, _ in enumerate(chars):
            if chars[idx] == chars[cursor]:
                count +=1
            elif count == 1:
                cursor += 1
                chars[cursor] = chars[idx]
            else:
                cursor += 1
                for digit in str(count):
                    chars[cursor] = digit
                    cursor += 1
                count = 1
                chars[cursor] = chars[idx]

        if count > 1:
            for digit in str(count):
                cursor += 1
                chars[cursor] = digit
        else:
            chars[cursor] = chars[-1]

        return cursor + 1


# chars = ["a", "b", "c", "d"]
# chars = ["a", "a", "a", "b", "c"]
# chars = ["a", "a", "b", "b", "c", "c", "c"]
# chars = ["a", "a", "a", "c", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b","b","b"]
print(chars)

sol = Solution()
print(chars[:sol.compress(chars)])

# YS07 TGY