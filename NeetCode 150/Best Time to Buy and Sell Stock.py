class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [-1 for i in range(len(prices))]
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j] - prices[i] > profits[i]:
                    profits[i] = prices[j] - prices[i]
        return max(profits) 
