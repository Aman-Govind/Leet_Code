# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        while root!=None:
            if root.val>val:
                root=root.left
            elif root.val<val:
                root=root.right
            elif root.val==val:
                return root
        return None

        