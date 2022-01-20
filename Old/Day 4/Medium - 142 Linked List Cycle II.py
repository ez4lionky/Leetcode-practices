# It is similar to 141.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        meet = None
        low = head
        fast = head
        while fast:
            low = low.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return None
            if fast is low:
                meet = fast
                break

        while head and meet:
            if head == meet:
                return head
            head = head.next
            meet = meet.next
        return None
