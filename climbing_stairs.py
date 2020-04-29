# https://leetcode.com/problems/climbing-stairs/
# you are climbing a stair case. It takes n steps
# to reach to the top.
# each time you can either climb 1 or 2 steps.
# in how many distinct ways can you climb to the top?

def climbStairs_1(n: int) -> int:
    if n == 0:
        return 0

    steps = {}
    def step_comb(i):
        if i in steps:
            return steps[i]
        elif i == 1 or i == 2:
            result = i
        else:
            result = step_comb(i - 2) + step_comb(i - 1)

        steps[i] = result
        return result

    return step_comb(n)

print(climbStairs_1(13))


def climbStairs_2(n: int) -> int:
    if n == 0 or n == 1 or n == 2:
        return n

    steps = [1, 2]

    for _ in range(3, n + 1):
        result = steps[0] + steps[1]
        steps[0], steps[1] = steps[1], result

    return result

print(climbStairs_2(13))


# SOLUTION:
# To get to n-th stair you can either take a single
# step from n-1th stair or a double step from
# n-2th stair, so the answer is the sum of combinations
# of steps to n-1 and n-2

# 1 =
# 1
#
# 2 =
# 11
# 2
#
# 3 =
# 111
# 12
# 21
#
# 4 =
# 1111
# 112
# 121
# 211
# 22
#
# 5 =
# 11111
# 1112
# 1121
# 1211
# 2111
# 221
# 212
# 122
#
# 6 =
# 111111
# 11121
# 11211
# 12111
# 21111
# 2211
# 2121
# 1221
# 11112
# 1122
# 1212
# 2112
# 222
