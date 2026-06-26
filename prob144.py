 #Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        current =root
        stack=[]
        result=[]

        while current or stack:
            if current:
                result.append(current.val)
                stack.append(current.right)
                current=current.left
            else:
                current=stack.pop()
        return result
        
        