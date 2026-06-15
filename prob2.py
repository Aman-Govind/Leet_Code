#Two linked list with numbers in reverse order, add them and return the sum as a linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        import numpy as np
        current1=l1
        current2=l2
        list1=[]
        list2=[]
        list3=[]
        carry=0

        while current1!=None:
            list1.append(current1.val)
            current1=current1.next
        while current2!=None:
            list2.append(current2.val)
            current2=current2.next
        if len(list1)>len(list2):
            diff =len(list1)
        else:
            diff=len(list2)
        for i in range (diff):
            if i<len(list1):
                a=list1[i]
            else:
                a=0
            if i<len(list2):
                b=list2[i]
            else:
                b=0
            sum=a+b+carry
            list3.append(sum%10)
            carry=sum//10
        if carry!=0:
            list3.append(carry)
            

        if not list3:
            return None
        head=ListNode(list3[0])
        current3=head

        for i in range (1,len(list3)):
            current3.next=ListNode(list3[i])
            current3=current3.next
        return head
