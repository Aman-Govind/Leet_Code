class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi=prices[0]
        ma=0
        for i in prices:
            if i<mi:
                mi=i
            else:
                profit=i-mi
                if profit>ma:
                    ma=profit
        return ma 
        