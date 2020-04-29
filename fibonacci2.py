from functools import lru_cache
# Least Recently Used Cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n has to be an integer")
    if n < 1:
        raise ValueError("n has to be a positive integer")

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 1001):
    print(i, ":", fibonacci(i))
