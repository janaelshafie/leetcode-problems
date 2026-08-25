# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if len(lists) <= 1:
            return lists[0] if lists else None

        m = len(lists) // 2

        list_l = self.mergeKLists(lists[:m])
        list_r = self.mergeKLists(lists[m:])

        return self.mergeTwoLists(list_l,list_r)

    def mergeTwoLists(self,listl,listr):
        curr_l = listl
        curr_r = listr
        dummy = node = ListNode()

        while curr_l and curr_r:
            if curr_l.val <= curr_r.val:
                node.next = curr_l
                curr_l = curr_l.next
            
            else:
                node.next = curr_r
                curr_r = curr_r.next
            
            node = node.next

        node.next = curr_l or curr_r

        return dummy.next

        