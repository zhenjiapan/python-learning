# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        res = ListNode()
        start = res
        carry = 0

        while (l1 is not None) or (l2 is not None) or carry != 0:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            digit = (x+y+carry) % 10
            carry = (x+y+carry) // 10

            res.next = ListNode(digit)
            res = res.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return start.next
