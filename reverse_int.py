# function that reverses an integer as in the example
# 321 -> 123

# def reverse_int(number):
# 	n = 0
# 	while True:
# 		if 10 ** n < abs(number):
# 			n += 1
# 		else:
# 			break

# 	result = 0
# 	num = number
# 	for i in range(n):
# 		result += 3
# 		3 == num // 10 ** 2
# 		result += num

# 		result += 20
# 		20 == (num - 300) // 10 ** 1

# 		result += 500
# 		500 == (num - 320) // 10 ** 0

# 		num %= 10 ** (n - i) ???

# 	return result

def reverse_int(number):
	isNegative = False
	if number < 0:
		isNegative = True

	int_as_string = str(abs(number))[::-1]

	result = int(int_as_string)

	if isNegative:
		result = -result

	if result < -2 ** 31 or result > 2 ** 31 - 1:
		return 0
	return result

print(reverse_int(1534236469))
