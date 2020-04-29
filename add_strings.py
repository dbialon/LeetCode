# https://leetcode.com/problems/add-strings/
# Given two non-negative integers num1 and num2
# represented as string, return the sum of num1 and num2.
# you must not use any built-in BigInteger library
# or convert the inputs to integer directly.

def addStrings_1(num1: str, num2: str) -> str:
	# much slower than method 2
    digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
    		"5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

    number1 = 0
    number2 = 0

    for i in range(len(num1)):
    	number1 += digits[num1[-1-i]] * 10 ** i

    for i in range(len(num2)):
    	number2 += digits[num2[-1-i]] * 10 ** i

    the_sum = number1 + number2

    result = ""

    while the_sum > 0:
    	letter = the_sum % 10
    	the_sum //= 10
    	for i in digits:
    		if digits[i] == letter:
    			result = i + result

    if result == "":
    	return "0"

    return result

def addStrings_2(num1: str, num2: str) -> str:
	# much faster than method 1
	digits = {str(i):i for i in range(10)}

	len1, len2 = len(num1), len(num2)

	if len1 > len2:
		num2 = "0" * (len1 - len2) + num2
	else:
		num1 = "0" * (len2 - len1) + num1

	number1 = []
	number2 = []

	for i in range(len(num1)):
		number1.append(digits[num1[i]])
		number2.append(digits[num2[i]])

	the_sum = []
	carrier = 0

	for i in range(len(number1)):
		num = number1[-1-i] + number2[-1-i] + carrier
		the_sum.append(num % 10)
		carrier = num // 10

	if carrier > 0:
		the_sum.append(carrier)

	result = ""

	for item in the_sum:
		result = "{}".format(item) + result

	return result

print(addStrings_1("1000", "1000"))
print(addStrings_2("1000","1000"))