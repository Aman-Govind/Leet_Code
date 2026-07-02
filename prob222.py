# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.right:
            return 1+self.countNodes(root.left)
        if not root.left:
            return 1+self.countNodes(root.right)
        return 1+self.countNodes(root.right)+self.countNodes(root.left)