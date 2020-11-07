# https://leetcode.com/problems/angle-between-hands-of-a-clock/
# Given two numbers, hour and minutes. Return the smaller angle
# (in degrees) formed between the hour and the minute hand.

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs((hour%12) * 30 - minutes * 5.5)
        return min(angle, 360 - angle)


solution = Solution()
for hour in range(1, 13):
    for minutes in (0, 15, 30, 45):
        print(f"{hour:02}:{minutes:02} {solution.angleClock(hour, minutes)}")
