# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        res = ListNode()
        head = res

        while list1 is not None or list2 is not None:
            if list1 is None:
                res.next = list2
                list2 = list2.next

            elif list2 is None:
                res.next = list1
                list1 = list1.next

            else:
                if list1.val <= list2.val:
                    res.next = list1
                    list1 = list1.next
                else:
                    res.next = list2
                    list2 = list2.next

            res = res.next

        return head.next