# https://leetcode.com/problems/repeated-substring-pattern/
# given a non-empty string check if it can be constructed
# by taking a substring of it and appending multiple
# copies of the substring together.
# You may assume the given string consists of lowercase
# English letters only and its length will not exceed 10000.

def repeatedSubstringPattern(s: str) -> bool:
    # empty list for characters' representations
    chars = []

    # turn each character into a numeric value
    for char in s:
        chars.append(ord(char))

    the_sum = sum(chars)
    length = len(chars)
    curr_sum = chars[0]

    # keep adding each item from the list until
    # sum of the whole list is divisible by the sum
    # of the slice
    for i in range(1, (len(chars) // 2) + 1):
        if the_sum % curr_sum == 0:
            # check if the slice is a substring o
            # the whole string
            if (length // i) * s[:i] == s:
                return True
        # add the value of another character
        curr_sum += chars[i]
    else:
        return False

my_string = "abcabcabc"
# my_string = "ababbaab"

print(repeatedSubstringPattern(my_string))
