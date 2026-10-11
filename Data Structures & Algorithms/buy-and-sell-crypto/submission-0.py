class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        size = len(prices)
        while(sell < size):
            profit = max(profit, prices[sell]-prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell
            sell +=1
        return profit