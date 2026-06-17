#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1=list(s)
        l2=list(t)
        l1.sort()
        l2.sort()
        if(l1==l2):
            return True
        else:
            return False
        
