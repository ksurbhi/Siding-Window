class Solution:
    # Time and Space Complexity: O(n) and O(1)
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
            else:
                i = j
            j = j +1
        return max_profit
        
