#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        # check if n is 0
        if n == 0:
            return False
        
        # divide n by 2, 3, and 5 until it is no longer divisible by 2, 3, and 5
        for i in [2, 3, 5]:
            while n % i == 0:
                n /= i
        
        # if n is 1, it is an ugly number
        return n == 1
        
# @lc code=end

