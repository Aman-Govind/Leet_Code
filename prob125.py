# 125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        substring=""
        for i in s:
            if i.isalnum():
                substring+=i
        return substring==substring[::-1]