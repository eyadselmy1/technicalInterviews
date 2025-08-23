class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]
        maxProfit = 0

        for i in range (0, len(prices)):
            if prices[i] > minPrice:
                maxProfit = maxProfit + (prices[i] - minPrice)
            minPrice = prices[i]

        return maxProfit
        