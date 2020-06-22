# https://leetcode.com/problems/validate-ip-address/

# Write a function to check whether an input string is a valid IPv4
# address or IPv6 address or neither.

# IPv4 addresses are canonically represented in dot-decimal notation,
# which consists of four decimal numbers, each ranging from 0 to 255,
# separated by dots ("."), e.g.,172.16.254.1;

# Besides, leading zeros in the IPv4 is invalid. For example, the address
# 172.16.254.01 is invalid.

# IPv6 addresses are represented as eight groups of four hexadecimal digits,
# each group representing 16 bits. The groups are separated by colons (":").
# For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334
# is a valid one. Also, we could omit some leading zeros among four
# hexadecimal digits and some low-case characters in the address to
# upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid
# IPv6 address(Omit leading zeros and using upper cases).

# However, we don't replace a consecutive group of zero value with a single
# empty group using two consecutive colons (::) to pursue simplicity.
# For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

# Besides, extra leading zeros in the IPv6 is also invalid. For example,
# the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

# Note: You may assume there is no extra space or special characters
# in the input string.

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if "." in IP and not ":" in IP and not ".." in IP:
            if IP[0] == "." or IP[-1] == ".":
                return "Neither"
            address = IP.split(".")
            if len(address) != 4:
                return "Neither"
            for number in address:
                if len(number) > 1 and number[0] == '0':
                    return "Neither"
                for digit in number:
                    if not 48 <= ord(digit) <= 57:
                        return "Neither"
                if not 0 <= int(number) <= 255:
                    return "Neither"
            return "IPv4"
        elif ":" in IP and not "." in IP and not "::" in IP:
            if IP[0] == '0' or IP[0] == ":" or IP[-1] == ":":
                return "Neither"
            address = IP.split(":")
            if len(address) != 8:
                return "Neither"
            for number in address:
                if len(number) > 4:
                    return "Neither"
                for digit in number:
                    if not 48 <= ord(digit) <= 57:
                        if not 'a' <= digit <= 'f':
                            if not 'A' <= digit <= 'F':
                                return "Neither"
            return "IPv6"
        else:
            return "Neither"


# address = "172.16.254.1" # "IPv4"
address = "2001:db8:85a3:0:0:8A2E:0370:7334" # "IPv6"

solution = Solution()
print(solution.validIPAddress(address))