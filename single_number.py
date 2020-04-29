# https://leetcode.com/problems/single-number/

# given a non-empty array of integers,
# every element appears twice except for one.
# find that single one

def singleNumber1(nums):
	result = 0
	for num in nums:
		# XOR operator
		result ^= num

	return(result)

def singleNumber2(nums):
	freq = dict()
	for num in nums:
		if num in freq:
			freq[num] += 1
		else:
			freq[num] = 1

	for item in freq:
		if freq[item] == 1:
			return item

alist = [5, 2, 3, 2, 3]
blist = [4, 1, 3, 1, 4]

print(singleNumber1(alist))
print(singleNumber1(blist))

print(singleNumber2(alist))
print(singleNumber2(blist))