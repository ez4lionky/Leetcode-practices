# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def LenListNode(head: ListNode) -> int:
    n = 0
    while head:
        n += 1
        head = head.next
    return n


def ForwardNNode(head, n):
    for i in range(n):
        head = head.next
    return head


class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1 = LenListNode(headA)
        len2 = LenListNode(headB)
        if len1 > len2:
            headA = ForwardNNode(headA, len1 - len2)
        else:
            headB = ForwardNNode(headB, len2 - len1)
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

