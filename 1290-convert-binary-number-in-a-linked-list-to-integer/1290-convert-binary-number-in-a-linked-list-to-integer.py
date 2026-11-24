# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        dec = 0
        while head:
            dec = (dec * 2) + head.val
            head = head.next

        return dec



        