class ListNode(object):
     def __init__(self, value, nextNode=None, prevNode=None):
        self.val = value
        self.next = nextNode
        self.prev = prevNode

class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_Node = ListNode(val)
        if self.tail == self.head:
            self.tail = new_Node
    
        new_Node.prev = self.head
        new_Node.next = self.head.next
        if self.head.next:
            self.head.next.prev = new_Node
        self.head.next = new_Node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_Node = ListNode(val)
        self.tail.next = new_Node
        new_Node.prev = self.tail
        self.tail = self.tail.next
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        new_Node = ListNode(val)
        curr = self.head.next
        i = 0
        while curr and i < index:
            i += 1
            curr = curr.next
        
        if curr and curr.prev:
            curr.prev.next = new_Node
            new_Node.prev = curr.prev
            new_Node.next = curr
            curr.prev = new_Node
        
        else:
            if i == index:
                self.addAtTail(val)
                return
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        curr = self.head.next
        i = 0
        while curr and i < index:
            i += 1
            curr = curr.next

        if not curr:
            return
        
        if curr and curr.next:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        else:
            self.tail = curr.prev
            self.tail.next = None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)