#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output=[]
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    output.append(i)
                    output.append(j)
        return output
        