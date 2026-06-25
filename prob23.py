# 23. Merge k Sorted Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        list1=[]
        for i in range(len(lists)):
            current=lists[i]
            while current!=None:
                list1.append(current.val)
                current=current.next
        if not list1:
            return None
        list1.sort()
        
        current2=ListNode(list1[0])
        head=current2
        current2.next=None
        for i in range (1,len(list1)):
            current2.next=ListNode(list1[i])
            current2=current2.next
        return head


        