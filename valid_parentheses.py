# https://leetcode.com/problems/valid-parentheses/
# Given a string containing just the characters '(', ')', '{', '}', '['
# and ']', determine if the input string is valid.
# An input string is valid if:
# * Open brackets must be closed by the same type of brackets.
# * Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

class Solution:
    # symbols = "()[]{}" # for string option
    symbols = {")": "(", "]": "[", "}": "{"} # for dictionary option
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True
        if len(s) & 1 == 1:
            return False

        # using a string
        # for idx, symbol in enumerate(s):
        #     for n in (1, 3, 5):
        #         if symbol == symbols[n]:
        #             if s[idx-1] == symbols[n-1]:
        #                 if len(s) == 2:
        #                     return True
        #                 else:
        #                     return self.isValid(s[:idx-1] + s[idx+1:])
        #             else:
        #                 return False

        # using a dictionary
        for idx, symbol in enumerate(s):
            if symbol in self.symbols:
                if s[idx-1] == self.symbols[symbol]:
                    if len(s) == 2:
                        return True
                    else:
                        return self.isValid(s[:idx-1] + s[idx+1:])
                else:
                    return False

####################
### TESTING ONLY ###
####################

# s = "()"
s = "()[]{}"
# s = "(]"
# s = "([)]"
# s = "{[]}"

solution = Solution()
print(solution.isValid(s))