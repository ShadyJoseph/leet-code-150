"""

The brute force way
performance n^2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                x = max(prices[j] - prices[i], x)

        return x

"""


# The Greedy Algo

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
