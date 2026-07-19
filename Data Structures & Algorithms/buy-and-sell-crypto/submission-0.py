class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find the day it is the highest
        # Find the day before that it is the lowest
        # Maximizing highest - lowest
        minimumSeen = max(prices)
        maxProfit = 0

        for day in prices:
            if day < minimumSeen:
                minimumSeen = day
                continue

            profit = day - minimumSeen
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit