# https://leetcode.com/problems/roman-to-integer/
# function to take a Roman number and return an integer
# equal to that number
# assume the number is no greater than 3,999

def roman_to_int_1(roman: str) -> int:
	result = 0

	if "IV" in roman: result -= 2 # IV is 4, not 6
	if "IX" in roman: result -= 2 # IX is 9, not 11
	if "XL" in roman: result -= 20 # XL is 40, not 60
	if "XC" in roman: result -= 20 # XC is 90, not 110
	if "CD" in roman: result -= 200 # CD is 400, not 600
	if "CM" in roman: result -= 200 # CM is 900, not 1100

	for letter in roman:
		if letter == "I": result += 1
		elif letter == "V": result += 5
		elif letter == "X": result += 10
		elif letter == "L": result += 50
		elif letter == "C": result += 100
		elif letter == "D": result += 500
		elif letter == "M": result += 1000

	return result


print(roman_to_int_1("XIX"), end="/")
print(roman_to_int_1("VI"), end="/")
print(roman_to_int_1("MCMLXXIX"))

def roman_to_int_2(roman: str) -> int:
	result = 0

	for i in range(len(roman)):
		if roman[i] == "I":
			result += 1
		elif roman[i] == "V":
			if i > 0 and roman[i-1] == "I":
				result += 3
			else:
				result += 5
		elif roman[i] == "X":
			if i > 0 and roman[i-1] == "I":
				result += 8
			else:
				result += 10
		elif roman[i] == "L":
			if i > 0 and roman[i-1] == "X":
				result += 30
			else:
				result += 50
		elif roman[i] == "C":
			if i > 0 and roman[i-1] == "X":
				result += 80
			else:
				result += 100
		elif roman[i] == "D":
			if i > 0 and roman[i-1] == "C":
				result += 300
			else:
				result += 500
		elif roman[i] == "M":
			if i > 0 and roman[i-1] == "C":
				result += 800
			else:
				result += 1000

	return result

print(roman_to_int_2("MCMXCVII"))
