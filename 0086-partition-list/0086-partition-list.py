# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:

        if head is None or head.next is None:
            return head

        SDummy = ListNode(0)
        GDummy = ListNode(0)
        small = SDummy
        great = GDummy
        curr = head
        
        while curr:
            if curr.val < x:
                small.next = curr
                small = curr

            else:
                great.next = curr
                great = curr

            curr = curr.next

        great.next = None
        small.next = GDummy.next

        return SDummy.next

        