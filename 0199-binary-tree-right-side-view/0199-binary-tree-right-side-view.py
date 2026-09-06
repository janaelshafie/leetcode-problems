from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        queue = deque()
        res = []
        if root:
            queue.append(root)
        
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()

                if i == (size - 1):
                    res.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)


        return res

        
        