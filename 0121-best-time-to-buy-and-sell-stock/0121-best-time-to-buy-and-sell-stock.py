class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        minimum = prices[0]

        for price in prices:
            minimum = min(minimum, price)
            current_profit = price - minimum
            profit = max(profit, current_profit)

        return max(0, profit)
