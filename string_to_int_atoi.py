# https://leetcode.com/problems/string-to-integer-atoi/
# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from
# this character takes an optional initial plus or minus sign followed
# by as many numerical digits as possible, and interprets them as
# a numerical value.
# The string can contain additional characters after those that form
# the integral number, which are ignored and have no effect on the behavior
# of this function.
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is
# empty or it contains only whitespace characters, no conversion is
# performed.
# If no valid conversion could be performed, a zero value is returned.
# Note:
# Only the space character ' ' is considered a whitespace character.
# Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−2**31,  2**31 − 1].
# If the numerical value is out of the range of representable values,
# INT_MAX (2**31 − 1) or INT_MIN (−2**31) is returned.


class Solution:
    def myAtoi(self, s: str) -> int:
        start = False
        number = []
        sign = 1
        for char in s:
            if not start:
                if char == " ":
                    pass
                elif char == "-":
                    sign = -1
                    start = True
                elif char == "+":
                    start = True
                elif char < "0" or char > "9":
                    return 0
                else:
                    number.append(char)
                    start = True
            else:
                if char >= "0" and char <= "9":
                    number.append(char)
                else:
                    break

        if not number:
            return 0

        ans = 0
        power = 0
        for digit in number[::-1]:
            ans += (ord(digit) - 48) * (10 ** power)
            power += 1

        ans *= sign

        if sign == 1:
            return min(2 ** 31 - 1, ans)
        else:
            return max(-2 ** 31, ans)


s = "      -53 one two three  "

solution = Solution()
print(solution.myAtoi(s))
