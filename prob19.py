# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        current1=head
        count=0
        while current1!=None:
            count+=1
            current1=current1.next
        count1=count-n
        current2=head
        count2=0
        if count==n:
            return head.next
        while current2!=None:
            if count2==count1-1:
                current2.next=current2.next.next
                break
            else:
                current2=current2.next
                count2+=1
        return head

        