# https://leetcode.com/problems/missing-number/

# given an array containing n distinct numbers
# taken from 0, 1, 2, ..., n, find the one
# that is missing from the array

def missingNumber(nums):
	length = len(nums)
	max_sum = length * (length + 1) // 2
	return max_sum - sum(nums)

alist = [0, 2, 1, 5, 7, 6, 9, 8, 4]
blist = [0]

print(missingNumber(alist))
print(missingNumber(blist))

# 1 + 2 + 3 + ... + n = n * (n + 1) / 2