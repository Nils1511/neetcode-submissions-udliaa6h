class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_point = []
        sell_point = []
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                buy_point.append(prices[i])
                sell_point.append(prices[i+1])

        sum = 0    
        for i in range(len(buy_point)):
            sum += sell_point[i] - buy_point[i]
        
        return sum


        