class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        res = 0
        for i in range(len(prices)):
            if prices[i] - prices[l]>0:
                res = max(res, prices[i] - prices[l])
            else:
                l = i
        return res