#PROBLEM LINK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Check if the prices array is empty
        if not prices:
            return 0
            
        # Initialize variables to keep track of minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0
        
        # Iterate through the prices array
        for price in prices:
            # Update min_price if the current price is smaller
            if price < min_price:
                min_price = price
            else:
                # Update max_profit by calculating the difference between the current price and min_price
                max_profit = max(max_profit, price - min_price)

        # Return the final max_profit
        return max_profit
    
#TIME COMPLEXITY: O(n)
#SPACE COMPLEXITY: O(1)