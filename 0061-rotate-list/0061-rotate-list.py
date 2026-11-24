# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None or k == 0:
            return head

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k = k % n
        if k == 0:
            return head

        tail.next = head
        newTail = head

        i = 1
        while i < n - k:
            newTail = newTail.next
            i += 1

        head = newTail.next
        newTail.next = None
        return head

        

        

        