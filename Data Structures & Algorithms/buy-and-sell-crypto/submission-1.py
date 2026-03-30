class Solution:
    #           val
    # [2,1,2,1,0,1,2]
    # Cheapest 1
    # Max 2
    # profit 
    # sec_Chep 0
    # sec_max 0
    # maximum_profit 1

    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = 101
        maximum_price = 0

        second_cheapers_price = 101
        second_maximum_price = 0

        maximum_profit = 0
        for i, val in enumerate(prices):
            if val < cheapest_price and maximum_price == 0:
                cheapest_price = val
                continue
            elif val < cheapest_price and maximum_price != 0 and val < second_cheapers_price:
                second_cheapers_price  = val
                continue

            if val > maximum_price:
                maximum_price = val
                profit = maximum_price - cheapest_price
                maximum_profit = profit

                if second_cheapers_price != 101:
                    second_maximum_price = val
                    second_profit = second_maximum_price - second_cheapers_price

                    if second_profit > profit:
                        maximum_profit = second_profit
                        cheapest_price = second_maximum_price
                        maximum_price = second_maximum_price
                        second_maximum_price = 0
                        second_maximum_price = 0

            elif val > second_maximum_price and second_cheapers_price != 101:
                second_maximum_price = val
                profit = second_maximum_price - second_cheapers_price

                if profit > maximum_profit:
                        maximum_profit = profit
                        cheapest_price = second_maximum_price
                        maximum_price = second_maximum_price
                        second_maximum_price = 0
                        second_maximum_price = 0

        return maximum_profit

            

        