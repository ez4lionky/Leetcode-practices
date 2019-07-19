# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head: ListNode, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head = ListNode(0)
        more_head = ListNode(0)
        less_ptr = less_head
        more_ptr = more_head
        while head:
            if head.val < x:
                less_ptr.next = head
                less_ptr = less_ptr.next
            else:
                more_ptr.next = head
                more_ptr = more_ptr.next
            head = head.next

        less_ptr.next = more_head.next
        more_ptr.next = None
        return less_head.next


a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

sol = Solution()
t = sol.partition(a, 3)
while t:
    print(t.val)
    t = t.next
