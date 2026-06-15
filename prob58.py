
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last=""
        text=s.rstrip()
        for c in text:
            if c==" ":
                last=""
            else:
                last+=c
        return len(last)