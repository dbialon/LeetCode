# https://leetcode.com/problems/count-and-say/
# given an integer n where 1 ≤ n ≤ 30, generate the nth term
# of the count-and-say sequence. You can do so recursively,
# in other words from the previous member read off the digits,
# counting the number of digits in groups of the same digit.
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
class Solution:
    cache = {}
    def countAndSay(self, n: int) -> str:
        if n in self.cache:
            return self.cache[n]

        if n == 1:
            self.cache[1] = "1"
            return "1"

        previous = self.countAndSay(n - 1)
        cursor = previous[0]
        counter = 1
        result = ""

        for i, value in enumerate(previous):
            if i == 0:
                continue
            if value == cursor:
                counter += 1
            else:
                result += str(counter) + cursor
                cursor = value
                counter = 1

        result += str(counter) + cursor

        self.cache[n] = result
        return result

sol = Solution()

for n in range(1, 31):
    print(f"{n}: {sol.countAndSay(n)}")