# Add first occurrence to the set and remove the second; the unique number remains.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u={}
        for i in range(len(nums)):

            if i in u:
                u.remove(nums[i])

            else:
                u.add(nums[i])
        s=u.pop
        return s