class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        profits = [0]
        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                hedge = prices[sell] - prices[buy]
                profits.append(hedge)
        return max(profits)
        
        # profits = [0]
        # for buy in range(len(prices) - 1):
        #     for i in range(len(prices) - 1):
        #         sell = i + 1

        #         if prices[sell] > prices[buy]:
        #             hedge = prices[sell] - prices[buy]
        #             profits.append(hedge)

        # return max(profits)


        #     for sell in range(len(prices)):

        #         if(prices[sell] > prices[buy]):
        #             hedge = prices[sell] - prices[buy]
        #             profits.append(hedge)
        # return max(profits)