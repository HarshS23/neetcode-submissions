class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profits = [0]
        minprice = prices[0]

        for buy in range(len(prices)):
            if minprice > prices[buy]:
                minprice = prices[buy]
            
            hedge = prices[buy] - minprice
            profits.append(hedge)
        
        return max(profits)



        # for buy in range(len(prices) - 1):
        #     sell = buy + 1
        #     if prices[sell] > prices[buy]:
        #         hedge = prices[sell] - prices[buy]
        #         profits.append(hedge)
        # return max(profits)

        # profits = [0]
        # for buy in range(len(prices)):
        #     for sell in range(buy + 1, len(prices)):

        #         hedge = prices[sell] - prices[buy]
        #         profits.append(hedge)
        # return max(profits)