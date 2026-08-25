from collections import deque
class MyStack(object):

    def __init__(self):
        self.q1 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        n = len(self.q1)
        self.q1.append(x)
        while n > 0:
            self.q1.append(self.q1.popleft())
            n -= 1

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()