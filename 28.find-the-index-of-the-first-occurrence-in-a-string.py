#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle is empty, return 0
        if not needle:
            return 0
        
        # if needle is not in haystack, return -1
        if needle not in haystack:
            return -1
        
        # return the index of the first occurrence of needle in haystack
        return haystack.index(needle)
        
# @lc code=end

