class ListNode:
    def __init__(self, value, nextNode = None):
        self.val = value
        self.next = nextNode

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1

        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_Node = ListNode(val)
        new_Node.next = self.head
        self.head = new_Node
        
        if self.tail is None:
            self.tail = new_Node

    def insertTail(self, val: int) -> None:
        new_Node = ListNode(val)
        if self.tail is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        
        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return True

        curr = self.head
        prev = None
        i = 0
        while i < index and curr:
            i += 1
            prev = curr
            curr = curr.next

        if prev and curr:
            if prev.next == self.tail:
                self.tail = prev
            prev.next = curr.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        res = []
        if self.head and self.tail:
            curr = self.head
            while curr:
                res.append(curr.val)
                curr = curr.next
        return res
        
