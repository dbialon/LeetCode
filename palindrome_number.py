# https://leetcode.com/problems/palindrome-number/
# determine whether an integer is a palindrome.
# n integer is a palindrome when it reads the same
# backward as forward, i.e. 121
# -121 is not a palindrome (121-)

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True

    number = []
    count = 0
    while x > 0:
        number.append(x % 10)
        x //= 10
        count += 1

    for i in range(count // 2):
        if number[i] != number[-1 - i]:
            return False

    return True

number = 789987

print(isPalindrome(number))
