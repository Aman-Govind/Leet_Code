# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stack1=[root.right]
        stack2=[root.left]
        while stack1 and stack2:
            curr1=stack1.pop()
            curr2=stack2.pop()
            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2:
                return False
            if curr1.val!=curr2.val:
                return False
            stack1.append(curr1.right)
            stack1.append(curr1.left)
            stack2.append(curr2.left)
            stack2.append(curr2.right)
        return True

        