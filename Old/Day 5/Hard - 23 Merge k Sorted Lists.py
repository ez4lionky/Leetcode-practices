# There are three methods:
# 1. Similar to the 21, compare k linked lists in turn, then add it into the last linked list.
# 2. Merge k lists into one disordered list, then sort it.
# 3. Fractional method, combine every 2 singly linked lists.
# Here is the implementation of the second and third methods.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        linked_list = []
        vals = []
        for h in lists:
            while h:
                vals.append(h.val)
                linked_list.append(h)
                h = h.next
        if len(linked_list) == 0:
            return None
        vals.sort()
        for i in range(len(vals)):
            if i != len(vals)-1:
                linked_list[i].next = linked_list[i+1]
            else:
                linked_list[i].next = None
            linked_list[i].val = vals[i]
        return linked_list[0]

