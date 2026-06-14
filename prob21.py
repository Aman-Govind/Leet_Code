#Merge two sorted linked list into a single sorted linked list
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1=[]
        p2=[]

        while list1:
            p1.append(list1.val)
            list1=list1.next
        while list2:
            p2.append(list2.val)
            list2=list2.next
        p3=p1+p2
        p3.sort()

        if len(p3)==0:
            return None
        head=ListNode(p3[0])
        current=head

        for i in range(1,len(p3)):
            current.next=ListNode(p3[i])
            current=current.next
        return head