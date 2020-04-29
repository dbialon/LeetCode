fibonacci_cache = {}

def fibonacci(n):
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	if n == 1:
		value = 0
	elif n == 2:
		value = 1
	else:
		value = fibonacci(n - 1) + fibonacci(n - 2)

	fibonacci_cache[n] = value
	return value

for i in range(1, 1001):
	print(f"{i}:", fibonacci(i))
