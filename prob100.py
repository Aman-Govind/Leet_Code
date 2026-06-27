# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        stack1=[p]
        stack2=[q]
        
        while stack1 and stack2:
            curr1=stack1.pop()
            curr2=stack2.pop()
            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2:
                return False
            if curr1.val!=curr2.val:
                 return False
            stack2.append(curr2.right)
            stack2.append(curr2.left)
            stack1.append(curr1.right)
            stack1.append(curr1.left)
        return True