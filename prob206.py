# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1=head
        lists=[]
        while temp1!=None:
            lists.append(temp1.val)
            temp1=temp1.next
        lists=lists[::-1]
        temp2=ListNode(0)
        current=temp2
        for i in lists:
            temp2.next=ListNode(i)
            temp2=temp2.next
        return current.next
        

        