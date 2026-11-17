class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for i in prices:
            if min_price > i:
                min_price = i 
            # max_profit = max(i-min_price,max_profit)
            if i-min_price > max_profit:
                max_profit = i-min_price
        return max_profit