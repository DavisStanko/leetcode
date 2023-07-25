#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create a variable to store the maximum profit
        max_profit = 0

        # create a variable to store the minimum price
        min_price = float('inf')

        # loop through each price
        for price in prices:
            # if the price is less than the minimum price
            if price < min_price:
                # update the minimum price
                min_price = price
            # if the price is greater than the minimum price
            else:
                # update the maximum profit
                max_profit = max(max_profit, price - min_price)
        
        return max_profit
        
# @lc code=end

