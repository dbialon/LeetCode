# https://leetcode.com/problems/add-two-numbers/
# you are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit.
# add the two numbers and return it as a linked list.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        nodes = []
        current = self.next
        while current:
            nodes.append(str(current.val))
            current = current.next

        return "[" + ", ".join(nodes) + "]"

    def append(self, val):
        if not self.next:
            self.next = ListNode(val=val)
            return
        current = self.next
        while current.next:
            current = current.next
        current.next = ListNode(val=val)

    def prepend(self, val):
        current = ListNode(val=val)
        current.next = self.next
        self.next = current

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(None)
    p, q = l1, l2
    cursor = result
    carrier = 0
    while p or q:
        if p:
            x = p.val
        else:
            x = 0
        if q:
            y = q.val
        else:
            y = 0
        the_sum = x + y + carrier
        carrier = the_sum // 10
        cursor.next = ListNode(the_sum % 10)
        cursor = cursor.next
        if p:
            p = p.next
        if q:
            q = q.next

    if carrier > 0:
        cursor.next = ListNode(carrier)

    return result.next

# [2,4,3] + [5,6,4] = [7,0,8]

l1 = ListNode(None)
l2 = ListNode(None)

l1.append(2)
l1.append(4)
l1.append(3)

l2.append(5)
l2.append(6)
l2.append(4)

l3 = ListNode(None)
l3.next = addTwoNumbers(l1.next, l2.next)

print(l1)
print(l2)
print(l3)
