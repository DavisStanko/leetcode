#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # create a list of fibonacci numbers
        fib = [1, 2]

        # loop through each number in the range
        for i in range(2, n):
            # append the sum of the previous two numbers
            fib.append(fib[i - 1] + fib[i - 2])

        # return the last number in the list
        return fib[n - 1]
        
# @lc code=end

