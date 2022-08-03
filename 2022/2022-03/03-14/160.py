# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         stackA, stackB = [], []
#         res = None
#         while headA:
#             stackA.append(headA)
#             headA = headA.next
#         while headB:
#             stackB.append(headB)
#             headB = headB.next
#         while stackA and stackB:
#             t1, t2 = stackA.pop(), stackB.pop()
#             if t1 == t2:
#                 res = t1
#         return res


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next

        while headB:
            if headB in s:
                return headB
            headB = headB.next
        return None

