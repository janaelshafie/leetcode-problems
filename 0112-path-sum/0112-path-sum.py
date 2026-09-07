# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        total = 0
        def p_sum(root, targetSum, total):
            if not root:
                return False
            
            total += root.val

            if not root.left and not root.right:
                if total == targetSum:
                    return True

            if p_sum(root.left, targetSum, total):
                return True

            if p_sum(root.right, targetSum, total):
                return True

            total -= root.val
            return False

        return p_sum(root, targetSum, total)


        