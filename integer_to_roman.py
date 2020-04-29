# https://leetcode.com/problems/integer-to-roman/

def intToRoman(num: int) -> str:
    number = []
    pow = 1
    while num > 0:
        number.append(pow * (num % 10))
        num //= 10
        pow *= 10

    result = ""

    for value in number:
        if value < 4:
            result = value * "I" + result
        elif value == 4:
            result = "IV" + result
        elif value < 9:
            result = "V" + (value - 5) * "I" + result
        elif value == 9:
            result = "IX"
        elif value < 40:
            result = (value // 10) * "X" + result
        elif value == 40:
            result = "XL" + result
        elif value < 90:
            result = "L" + ((value - 50) // 10) * "X" + result
        elif value == 90:
            result = "XC" + result
        elif value < 400:
            result = (value // 100) * "C" + result
        elif value == 400:
            result = "CD" + result
        elif value < 900:
            result = "D" + ((value - 500) // 100) * "C" + result
        elif value == 900:
            result = "CM" + result
        elif value < 4000:
            result = (value // 1000) * "M" + result

    return result

number = 1994

print(intToRoman(number))
