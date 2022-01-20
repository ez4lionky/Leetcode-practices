# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode):
    num1, num2 = '', ''
    datap = l1
    while datap is not None:
        num1 = num1 + str(datap.val)
        datap = datap.next
    datap = l2
    while datap is not None:
        num2 = num2 + str(datap.val)
        datap = datap.next
    num1 = num1[::-1]
    num2 = num2[::-1]
    return create_node_list(str(int(num1) + int(num2)))


def create_node_list(s):
    s = s[::-1]
    nl = ListNode()
    p = nl
    for idx, i in enumerate(s):
        p.val = int(i)
        if idx == len(s) - 1:
            p.next = None
        else:
            tmp = ListNode()
            p.next = tmp
            p = tmp
    return nl


t1 = create_node_list('342')
t2 = create_node_list('465')
result = addTwoNumbers(t1, t2)
while result is not None:
    print(result.val)
    result = result.next
