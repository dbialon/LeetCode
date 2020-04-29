# https://leetcode.com/problems/implement-strstr/
# return the index of the first occurrence of needle
# in haystack, or -1 if needle is not part of haystack.

def strStr(haystack: str, needle: str) -> int:
    l = len(needle)

    if l == 0:
        return 0

    if needle not in haystack:
        return -1

    for i in range(len(haystack)):
        if haystack[i:i+l] == needle:
            return i

    return -1

needle = "ll"

haystack = "hello"

print(strStr(haystack, needle))
