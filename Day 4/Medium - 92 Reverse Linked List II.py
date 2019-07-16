class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = None
        result = head
        for i in range(m-1):
            pre = head
            head = head.next
        new_list_tail = head
        new_list_head = None
        for i in range(n-m+1):
            next = head.next
            head.next = new_list_head
            new_list_head = head
            head = next
        new_list_tail.next = head
        if pre:
            pre.next = new_list_head
        else:
            result = new_list_head
        return result


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
head = a
m = 2
n = 4

sol = Solution()
m = 2
n = 4
t = sol.reverseBetween(head, m, n)
while t:
    print(t.val)
    t = t.next
