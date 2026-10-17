class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit ,left_max = -1 , -1
        for i in range(len(prices) -1,-1,-1):
            left_max = max(left_max,prices[i])
            max_profit = max(max_profit , left_max - prices[i])
        
        return max_profit

        