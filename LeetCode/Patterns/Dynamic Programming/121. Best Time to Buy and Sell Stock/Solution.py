class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        max_prof = 0
        for i in range(1, len(prices)):
            if prices[i] == 0:
                continue

            if buy_price > prices[i]:
                buy_price = prices[i]
                continue
            if buy_price < prices[i] and prices[i] - buy_price > max_prof: 
                max_prof = prices[i] - buy_price
        return max_prof
