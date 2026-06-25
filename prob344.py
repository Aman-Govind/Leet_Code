class Solution(object):
    def reverseString(self, s):
        t = s[:]      
        p = len(s) - 1

        i = 0
        while p >= 0:
            s[i] = t[p]
            p -= 1
            i += 1
            #or
            #s.reverse()