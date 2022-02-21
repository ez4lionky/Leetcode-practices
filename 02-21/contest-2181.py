# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        pre = head
        while pre.next:
            if pre.val == 0:
                v = 0
                cur = pre
                while cur.next.val != 0:
                    v += cur.val
                    cur = cur.next
                pre.val = v + cur.val
                if cur.next.next:
                    pre.next = cur.next
                    pre = cur.next
                else:
                    pre.next = None
        return head
