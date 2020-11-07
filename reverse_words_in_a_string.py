# https://leetcode.com/problems/reverse-words-in-a-string/
# Given an input string, reverse the string word by word.
# Note:
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However,
# your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single
# space in the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word for word in s.split(" ") if word][::-1])


s = "    the  sky        is blue                             "

solution = Solution()
print(f"\'{solution.reverseWords(s)}\'")
