# https://leetcode.com/problems/day-of-the-week/
# Given a date, return the corresponding day of the week for that date.
# The input is given as three integers representing the day, month
# and year respectively.
# Return the answer as one of the following values
# {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
# The given dates are valid dates between the years 1971 and 2100.


class Solution:
    def __init__(self):
        # 2100 is not a leap year so it's not included
        self.leap = {x for x in range(1971, 2100) if x % 4 == 0}
        # o1/o1/71 was a Friday (day 1) so Thursday is day 0
        self.d = ["Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday"]
        # no. of days in each month
        self.m = [31,28,31,30,31,30,31,31,30,31,30,31]
        

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        count = 0
        for y in range(1971, year):
            if y in self.leap:
                count += 366
            else:
                count += 365
        if year in self.leap:
            if month > 2:
                count += 1
        for i in range(month-1):
            count += self.m[i]
        count += day
        return self.d[count % 7]


day, month, year = 19, 6, 1999

solution = Solution()
print(solution.dayOfTheWeek(day, month, year))
