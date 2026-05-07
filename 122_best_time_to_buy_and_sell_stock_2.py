"""
Peak-valley approach
find every valley local min and peak local max

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices) - 1
        i = 0
        peak = 0
        valley = 0

        while i < n:
            # find valley (go down)
            while i < n and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]

            # find peak (go up)
            while i < n and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]

            profit += peak - valley

        return profit


"""

# Greedy Algo the optimal solution
# time complexity n
# space complexity 1


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i]-prices[i-1])
        return profit
