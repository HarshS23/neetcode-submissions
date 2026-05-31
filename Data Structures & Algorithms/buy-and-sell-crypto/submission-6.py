class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profits = [0]
        minprice = prices[0]

        for buy in range(len(prices)): # -- O(n)
            if minprice > prices[buy]:
                minprice = prices[buy]
            
            hedge = prices[buy] - minprice
            profits.append(hedge)
        
        return max(profits)
