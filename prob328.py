# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head :
            return None
        current=head
        current1=head.next
        temp=ListNode(0)
        dummy=temp
        while current!=None:
            temp.next=ListNode(current.val)
            temp=temp.next
            if current.next!=None and current.next.next!=None:

                current=current.next.next
            else:
                break

        while current1!=None:
            temp.next=ListNode(current1.val)
            temp=temp.next
            if current1.next!=None and current1.next.next!=None:

                current1=current1.next.next
            else:
                break
        return dummy.next