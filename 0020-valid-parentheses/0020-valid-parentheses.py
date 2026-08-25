class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = { ')': '(', ']': '[', '}': '{'}     
        for string in s:
            if string in '([{':
                stack.append(string)
            elif string in ')]}':
                if not stack or stack[-1] != pairs[string]:
                    return False
                stack.pop()
        return not stack
        