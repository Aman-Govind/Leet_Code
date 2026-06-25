class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        count0=nums.count(0)
        count1=nums.count(1)
        count2=nums.count(2)
        j=0
        k=0
        m=0
        i=0
        while i<=len(nums):
            if j<count0:
                nums[i]=0
                j+=1
            elif k<count1:
                nums[i]=1
                k+=1
            elif m<count2:
                nums[i]=2
                m+=1
            i+=1
                        
            
