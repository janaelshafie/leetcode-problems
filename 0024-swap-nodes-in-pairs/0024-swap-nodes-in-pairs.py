# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:

        dummy = ListNode(0,head)

        prev = dummy

        while prev.next and prev.next.next:
            left = prev.next
            right = prev.next.next

            left.next = right.next
            right.next = left
            prev.next = right

            prev = left

        return dummy.next
        