# https://leetcode.com/problems/multiply-strings/
# given two non-negative integers num1 and num2 represented
# as strings, return the product of num1 and num2, also
# represented as a string.

def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    table = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6":6, "7": 7,
            "8": 8, "9": 9, "0": 0}

    n_1, n_2 = 0, 0
    l1,  l2  = len(num1), len(num2)

    for i in range(l1):
        n_1 += table[num1[i]] * 10 ** (l1 - i - 1)

    for i in range(l2):
        n_2 += table[num2[i]] * 10 ** (l2 - i - 1)

    result = n_1 * n_2

    num3 = ""
    while result > 0:
        # for key, value in table.items():
        #     if result % 10 == value:
        #         num3 = key + num3
        num3 = chr(48 + result % 10) + num3
        result //= 10

    return num3

str_1 = "12312312312312312312313123123123123123123123123123123123"
str_2 = "13213213213213213213232132132132132132132132132132132132"

print(multiply(str_1, str_2))
