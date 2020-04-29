# compute and return the square root of x,
# where x is guaranteed to be a non-negative integer.
# since the return type is an integer,
# the decimal digits are truncated and
# only the integer part of the result is returned.

def mySqrt(x: int) -> int:
        i = 0
        while i * i < x:
            i += 1
        
        if i * i == x:
            return i
        return i - 1

num = 19
print(mySqrt(num))