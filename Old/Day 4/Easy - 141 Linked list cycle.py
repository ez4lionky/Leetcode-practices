# The key idea is simulate the idea of running race.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        low = head
        fast = head
        while fast:
            low = low.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False
            if fast is low:
                return True

        if fast is None:
            return False


sol = Solution()
