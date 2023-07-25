#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split the string into a list
        s = s.split()
        
        # if the list is empty, return 0
        if not s:
            return 0
        
        # return the length of the last item in the list
        return len(s[-1])
        
# @lc code=end

