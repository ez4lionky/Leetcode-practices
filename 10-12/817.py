# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        res, inSet = 0, False
        while head:
            if head.val not in nums:
                inSet = False
            elif not inSet:
                inSet = True
                res += 1
            head = head.next
        return res

