#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert binary to decimal
        a = int(a, 2)
        b = int(b, 2)
        
        # add the two numbers
        answer = a + b
        
        # convert decimal to binary
        answer = bin(answer)
        
        # remove the '0b' at the beginning of the string
        answer = answer[2:]
        
        return answer
        
# @lc code=end

