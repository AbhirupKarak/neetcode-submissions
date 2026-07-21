class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        minPrice = max(prices)
        #run a loop to find minimum value on the left side of every ith price
        for i, price in enumerate(prices): 
            minPrice = min(price, minPrice)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit



        