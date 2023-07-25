#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert list to string
        digits = ''.join(map(str, digits))
        
        # convert string to integer
        digits = int(digits)
        
        # add one
        digits += 1
        
        # convert integer to string
        digits = str(digits)
        
        # convert string to list
        digits = list(digits)
        
        # convert list to integer
        digits = list(map(int, digits))
        
        return digits
        
# @lc code=end

