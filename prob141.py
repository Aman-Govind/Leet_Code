
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current=head
        lists=set()

        while current!=None:
            if current in lists:
                return True
            else:
                lists.add(current)
                current=current.next
        return False
