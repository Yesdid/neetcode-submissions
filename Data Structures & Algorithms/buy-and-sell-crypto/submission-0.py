class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for day in range(len(prices)):
            for next_day in range(day + 1, len(prices)):
                if(max_profit < (prices[next_day] - prices[day])):
                    max_profit = prices[next_day] - prices[day]

        return max_profit
        