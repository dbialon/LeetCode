# https://leetcode.com/problems/plus-one/
# given a non-empty array of digits representing a non-negative
# integer, plus one to the integer.
# the digits are stored such that the most significant
# digit is at the head of the list, and each element in the array
# contains a single digit.

def plusOne(digits: [int]) -> [int]:
	n = len(digits) - 1
	while n > -1:
		if digits[n] == 9:
			digits[n] = 0
		else:
			digits[n] += 1
			return digits
		n -= 1

	if digits[0] == 0:
		digits.insert(0, 1)

	return digits

integer = [9, 9, 9, 0, 0, 9, 9, 9]

print(integer, end="")
print(" -->", plusOne(integer))