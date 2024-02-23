#PROBLEM LINK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans+=prices[i] -prices[i-1]
        return ans
        
        
#time complexity is O(n)
#space complexity is O(1)