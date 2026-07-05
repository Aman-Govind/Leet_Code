# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[]
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            return res
        lists=inorder(root)
        list1=[]
        mini=999999
        for i in range(len(lists)):
            for j in range (i+1,len(lists)):
                if abs(lists[i]-lists[j])<mini:
                    mini=abs(lists[i]-lists[j])
        
        return mini
