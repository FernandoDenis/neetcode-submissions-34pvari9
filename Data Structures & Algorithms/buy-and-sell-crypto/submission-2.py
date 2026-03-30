class Solution:
    #             lr
    # [10,1,5,6,7,1]
    # max_profit 6

    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        maximum_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maximum_profit = max(maximum_profit, profit)
            else:
                l = r
            r += 1

        return maximum_profit

            

        