class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            maxProfit = max(maxProfit, price-minPrice)
            minPrice = min(minPrice, price)

        return maxProfit
        