# https://leetcode.com/problems/number-of-1-bits/submissions/7
# count '1' bits in a non-negative integer

def HammingWeight(n):
	count = 0
	while n > 0:
		if n & 1 == 1:
			count += 1
		n >>=  1

	return count


def count_1_bits(n):
    bits_as_string = str(bin(n))
    
    count = 0
    for bit in bits_as_string:
        if bit == "1":
            count += 1

    return count

number = 1243

print(count_1_bits(number))
print(HammingWeight(number))
print(number, bin(number))


# Hamming Weight method checks the value of the first bit,
# n & 1 returns 1 if the bit is '1' and '0' otherwise
# the bits are then shifted to the right by 1 bit
# this continues until the number is shifted all the way to 0
# count_1_bits - brute force method
# converts an integer into a binary
# then into a string
# go through the characters one by one
# and count occurences of '1'