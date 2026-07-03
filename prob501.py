# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        maxi=0
        list1=[]
        for i in res:
            if res.count(i)>maxi:
                maxi=res.count(i)
                list1=[i]
            elif res.count(i)==maxi and i not in list1:
                list1.append(i)
        return list1