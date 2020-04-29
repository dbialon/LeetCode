# https://leetcode.com/problems/n-th-tribonacci-number/
# tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2
# for n >= 0.
# given n, return the value of Tn.

from functools import lru_cache

@lru_cache(maxsize=1000)
def trib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return trib(n - 1) + trib(n - 2) + trib(n - 3)

print(trib(19))

def tribonacci(n: int) -> int:
    trib = [0, 1, 1]
    for i in range(3, n + 1):
        trib.append(trib[i - 1] + trib[i - 2] + trib[i - 3])

    return trib[n]

print(tribonacci(19))
