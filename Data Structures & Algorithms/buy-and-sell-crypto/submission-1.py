class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumSeen = None
        maxProfit = 0

        for day in prices:
            if minimumSeen is None:
                minimumSeen = day
                continue
            if day < minimumSeen:
                minimumSeen = day
                continue

            profit = day - minimumSeen
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit