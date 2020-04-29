# https://leetcode.com/problems/reverse-bits

# correct output: 43261596 returns 964176192

def reverseBits(n):
    reversedBinary = 0
    # unsigned int is 32 bits long
    for _ in range(32):
        # shift the reversed number 1 bit to the left
        # to prepare 'space' for the first bit of n
        reversedBinary = reversedBinary << 1
        # store the first bit of n in buffer
        buffer = n & 1
        # shift n 1 bit to the right (get rid of the first bit)
        n = n >> 1
        # change the first 'empty' bit of n to what's in buffer
        reversedBinary = reversedBinary | buffer

    return reversedBinary

def reverse_binary(n):
    # turn bits into a string
    n = str(bin(n))

    # get rid of '0b'
    n = n[2:]
    
    # n is a 32-bits unsigned integer
    # bin(n) removed leading 0's at the beginning
    # of the number
    # add missing '0' bits
    leading_bits = 32 - len(n)
    n = leading_bits * "0" + n
    
    # reverse the string
    n = n[::-1]
    
    # add '0b'
    n = "0b" + n
    
    # turn it into an int    
    return int(n, 2)

number = 43261596

print(reverseBits(number))
print(reverse_binary(number))