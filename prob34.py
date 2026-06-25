# 34. Find First and Last Position of Element in Sorted Array
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left=0
        right=len(nums)-1
        if len(nums)==1 and nums[0]==target:
            return [0,0]
        while left<right:
            if nums[left]<target:
                left+=1
            if nums[right]>target:
                right-=1
            if nums[right]==target and nums[left]==target:
                return [left,right]

       
        return [-1,-1]
        
