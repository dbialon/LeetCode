# https://leetcode.com/problems/count-primes/
# count the number of prime numbers less than
# a non-negative number, n

def countPrimes(n: int) -> int:
	count = 0
	multiples = dict()
	for num in range(2, n):
		if num not in multiples:
			count += 1
			for compound in range(num * num, n, num):
				multiples[compound] = True

	print(multiples)
	return count

print(countPrimes(10))