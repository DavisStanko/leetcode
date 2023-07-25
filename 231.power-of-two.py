#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # check if n is a power of two
        # if n is a power of two, return True
        # else, return False
        
        # if n is less than 1, return False
        if n < 1:
            return False
        
        # if n is equal to 1, return True
        if n == 1:
            return True
        
        # if n is greater than 1, keep dividing n by 2
        while n > 1:
            n /= 2
        
        # if n is equal to 1, return True
        if n == 1:
            return True
        
        # else, return False
        return False
        
# @lc code=end

