# https://leetcode.com/problems/add-binary/
# given two binary strings, return their sum
# (also a binary string).
# the input strings are both non-empty and contains only characters 1 or 0.

def addBinary1(a: str, b: str) -> str:
	a = "0b" + a
	b = "0b" + b

	the_sum = int(a, 2) + int(b, 2)

	return bin(the_sum)[2:]

def first_bit(num: int) -> int:
	if num & 1 == 0:
		return 0
	return 1

def addBinary2(a: str, b: str) -> str:
	a = int(a, 2)
	b = int(b, 2)

	carrier = 0
	bkwrds = ""

	while a > 0 or b > 0:
		if first_bit(a) == 1 and first_bit(b) == 1:
			if carrier == 1:
				bkwrds += "1"
			else:
				bkwrds += "0"
			carrier = 1
		elif first_bit(a) == 0 and first_bit(b) == 0:
			if carrier == 1:
				bkwrds += "1"
			else:
				bkwrds += "0"
			carrier = 0
		else:
			if carrier == 1:
				bkwrds += "0"
				carrier = 1
			else:
				bkwrds += "1"
				carrier = 0
		a = a >> 1
		b = b >> 1

	if carrier == 1:
		bkwrds += str(carrier)

	if bkwrds == "":
		return "0"

	return bkwrds[::-1]

print(addBinary1("110111", "1"))
print(addBinary2("0", "0"))