# Remove all occurrences of val from nums in-place and return the count of remaining elements.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        list1=[]
        for i in nums:
            if(i!=val):
                list1.append(i)
        for j in range (len(list1)):
            nums[j]=list1[j]
        return len(list1)