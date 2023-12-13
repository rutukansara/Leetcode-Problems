
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        # iterate through the prices
        for price in prices[1:]:
            # update the minimum price if a lower price is found
            min_price = min(min_price, price)
            # update the maximum profit if a higher profit is found
            max_profit = max(max_profit, price - min_price)

        return max_profit