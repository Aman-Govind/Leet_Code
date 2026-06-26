# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        result=[]
        stack=[root]
        visted=[False]
        while  stack:
            current=stack.pop()
            vis=visted.pop()
            if current:
                if vis:
                    result.append(current.val)
                else:
                    stack.append(current)
                    visted.append(True)
                    stack.append(current.right)
                    visted.append(False)
                    stack.append(current.left)
                    visted.append(False)
        return result

           