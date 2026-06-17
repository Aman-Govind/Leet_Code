#Palindrome Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        l1=head
        list1=[]
        while l1 != None:
            list1.append(l1.val)
            l1=l1.next
        if list1==list1[::-1]:
            return True
        else:
            return False

