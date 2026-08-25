class ListNode(object):
    def __init__(self, value, nextNode=None, prevNode=None):
        self.val = value
        self.next = nextNode
        self.prev = prevNode

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """ 
        self.point = ListNode(homepage)


    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_page = ListNode(url)
        new_page.prev = self.point
        self.point.next = new_page
        self.point = self.point.next
            

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """      
        while self.point.prev and steps > 0:
            self.point = self.point.prev
            steps -= 1

        return self.point.val

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.point.next and steps > 0:
            self.point = self.point.next
            steps -= 1

        return self.point.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)