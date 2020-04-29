# https://leetcode.com/problems/length-of-last-word/
# given a string s consists of upper/lower-case alphabets
# and empty space characters ' ', return the length of
# last word (last word means the last appearing word
# if we loop from left to right) in the string.
# if the last word does not exist, return 0.

def lengthOfLastWord(s: str) -> int:
	while len(s) > 0 and s[-1] == " ":
		s = s[:-1]

	if len(s) == 0:
		return 0

	aString = s.split(' ')

	return len(aString[-1])

my_string = "a     b   "

print(lengthOfLastWord(my_string))