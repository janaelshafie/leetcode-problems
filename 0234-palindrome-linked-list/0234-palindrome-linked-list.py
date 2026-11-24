# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next #fast pointer
            slow = slow.next #slow pointer

        mid = slow
        prev = None

        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt

        left = head
        right = prev
        while right:
            if right.val != left.val:
                return False
            
            right = right.next
            left = left.next

        return True




        