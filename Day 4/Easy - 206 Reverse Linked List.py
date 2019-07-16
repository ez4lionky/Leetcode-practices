# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_list_head = None
        next = ListNode(0)
        while head:
            next = head.next
            head.next = new_list_head
            new_list_head = head
            head = next
        return new_list_head
