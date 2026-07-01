# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sum=0
        if not root:
            return 0
        if root.left:
            if not root.left.left and not root.left.right:
                sum+=root.left.val
        sum+= self.sumOfLeftLeaves(root.left)
        sum+=self.sumOfLeftLeaves(root.right)
        return sum