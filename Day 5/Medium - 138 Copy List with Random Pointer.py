# The key idea is using dict to store the corresponding order of nodes.
# and using the list to recover the original connection between nodes.
"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        random_dict = {}
        ptr = head
        copy_list = []
        i = 0
        while ptr:
            random_dict[ptr] = i
            tmp = Node(ptr.val, None, None)
            copy_list.append(tmp)
            ptr = ptr.next
            i += 1

        ptr = head
        i = 0
        while ptr:
            if i != len(copy_list) - 1:
                copy_list[i].next = copy_list[i+1]
            else:
                copy_list[i].next = None
            if ptr.random:
                copy_list[i].random = copy_list[random_dict[ptr.random]]
            else:
                copy_list[i].random = None
            ptr = ptr.next
            i += 1
        if copy_list:
            return copy_list[0]
        else:
            return None
