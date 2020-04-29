# https://leetcode.com/problems/counting-bits/
# given a non negative integer number num
# for every i in the range 0 ≤ i ≤ num calculate the number of 1's
# in their binary representation and return them as an array
# Input: 5 Output: [0, 1, 1, 2, 1, 2]

def countBits(num):
	bits_array = []
	for i in range(num + 1):
		if i == 0:
			bits_array.append(i)
		elif i & 1 == 1:
			bits_array.append(bits_array[-1] + 1)
		else:
			bits_array.append(bits_array[i//2])

	return bits_array

number = 32

for count, item in enumerate(countBits(number)):
	print(f"{count:03} {item}")

print(countBits(number))

#  i binary   set
#  0 0b0000    0	set bits equal to i
#  1 0b0001    1	for odd nums set bits equal to 1 + set bits of the previous number
#  2 0b0010    1	for even nums set bits equal to set bits of i / 2
#  3 0b0011    2	add 1 to "2"
#  4 0b0100    1	same as "2"
#  5 0b0101    2	add 1 to "4"
#  6 0b0110    2	and so on...
#  7 0b0111    3
#  8 0b1000    1
#  9 0b1001    2
# 10 0b1010    2
# 11 0b1011    3
# 12 0b1100    2
# 13 0b1101    3
# 14 0b1110    3
# 15 0b1111    4
