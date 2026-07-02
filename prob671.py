# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[]
        def postorder(root):
            if not root:
                return 
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        lists=list(set(res))
        mini=min(lists)
        lists.remove(mini)
        if not lists:
            return -1
        return min(lists)
        