# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def evaluateTree(self, root):
        stack = [root]
        visited = [False]
        result = []

        while stack:
            curr = stack.pop()
            visit = visited.pop()

            if curr:
                if visit:
                    if curr.val == 0:
                        result.append(False)
                    elif curr.val == 1:
                        result.append(True)
                    elif curr.val == 2:      
                        right = result.pop()
                        left = result.pop()
                        result.append(left or right)
                    else:                    
                        right = result.pop()
                        left = result.pop()
                        result.append(left and right)
                else:
                    stack.append(curr)
                    visited.append(True)

                    stack.append(curr.right)
                    visited.append(False)

                    stack.append(curr.left)
                    visited.append(False)

        return result.pop()