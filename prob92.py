# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        temp=head
        list1=[]
        while(temp!=None):
            list1.append(temp.val)
            temp=temp.next
        list2=[]
        for i in range(left-1,right):
            list2.append(list1[i])
        list2=list2[::-1]
        j=0
        for i in range(left-1,right):
            list1[i]=list2[j]
            j=j+1
        
        current=ListNode(list1[0])
        temp1=current
        for i in range(1,len(list1)):
            current.next=ListNode(list1[i])
            current=current.next
        return temp1
        



