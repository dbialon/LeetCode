# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/
# 540/week-2-june-8th-june-14th/3355/

# Given a string s and a string t, check if s is subsequence of t.
# A subsequence of a string is a new string which is formed from
# the original string by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters.
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        if len(t) < len(s):
            return False
        for letter in s:
            if letter in t[idx:]:
                idx += t[idx:].index(letter) + 1
            else:
                return False
        else:
            return True


# s = "abc"
# t = "ahbgdc"

# s = "axc"
# t = "ahbgdc"

# s = "ubune"
# t = "subsequence"

s = "wittdtubnterltivsitionstheniac"
t = "without disturbing the relative positions of the remaining characters"

solution = Solution()
print(solution.isSubsequence(s, t))