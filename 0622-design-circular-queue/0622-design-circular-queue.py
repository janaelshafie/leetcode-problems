class ListNode(object):
    def __init__(self, value, nextNode=None, prevNode=None):
        self.val = value
        self.next = nextNode


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.n = 0
        self.head = None
        self.tail = None



    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        new_Node = ListNode(value)

        if self.isEmpty():
            self.head = new_Node
            self.tail = new_Node

        else:
            self.tail.next = new_Node
            self.tail = new_Node

        self.tail.next = self.head

        self.n += 1        
        return True


    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        if self.n == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        self.n -= 1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        return self.head.val if self.n > 0 else -1
        

    def Rear(self):
        """
        :rtype: int
        """
        return self.tail.val if self.n > 0 else -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.n == 0:
            return True
        
        return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.n == self.size:
            return True

        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()