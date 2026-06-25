# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        list1=[]
        current=head
        if not head:
            return None
        while current!=None:
            if current.val!=val:
                list1.append(current.val)
            current=current.next
        head1=ListNode(0)
        current1=head1
        for i in list1:
            current1.next=ListNode(i)
            current1=current1.next
        return head1.next 
        