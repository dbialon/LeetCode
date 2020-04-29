# https://leetcode.com/problems/repeated-string-match/submissions/
# given two strings A and B, find the minimum number of times
# A has to be repeated such that B is a substring of it.
# If no such solution, return -1.
# example, with A = "abcd" and B = "cdabcdab".
# return 3, because by repeating A three times (“abcdabcdabcd”),
# B is a substring of it; and B is not a substring of A
# repeated two times ("abcdabcd").
# the length of A and B will be between 1 and 10000.

def repeatedStringMatch(self, A: str, B: str) -> int:
    len_a = len(A)
    len_b = len(B)
    for i in range(1, 10_001):
        if B in i * A:
            return i
        # check if i * len(A) is more than twice len(B)
        # and i > 2 which means that at least one
        # concatenation has taken place
        elif i * len_a > 2 * len_b and i > 2:
            return -1
    else:
        return -1
