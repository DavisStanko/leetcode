#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # check if n is a power of 2
        if n <= 0 or n & (n - 1) != 0:
            return False
        
        # check if n is a power of 4
        return n & 0x55555555 == n
        
# @lc code=end

