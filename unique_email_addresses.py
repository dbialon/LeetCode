# https://leetcode.com/problems/unique-email-addresses/
# Every email consists of a local name and a domain name, separated
# by the @ sign.
# For example, in alice@leetcode.com, alice is the local name, and
# leetcode.com is the domain name.
# Besides lowercase letters, these emails may contain '.'s or '+'s.
# If you add periods ('.') between some characters in the local name part
# of an email address, mail sent there will be forwarded to the same
# address without dots in the local name. For example, "alice.z@leetcode.com"
# and "alicez@leetcode.com" forward to the same email address.
# (Note that this rule does not apply for domain names.)
# If you add a plus ('+') in the local name, everything after the first
# plus sign will be ignored. This allows certain emails to be filtered,
# for example m.y+name@email.com will be forwarded to my@email.com.
# (Again, this rule does not apply for domain names.)
# It is possible to use both of these rules at the same time.
# Given a list of emails, we send one email to each address in the list.
# How many different addresses actually receive mails?

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            domain = email.split('@')[1]
            loc_name = []
            for char in email:
                if char == '+' or char == '@':
                    break
                elif char != '.':
                    loc_name.append(char)
            loc_name = ''.join(loc_name)
            email = loc_name + '@' + domain
            unique.add(email)
            
        return len(unique)


emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]

solution = Solution()
print(solution.numUniqueEmails(emails))
