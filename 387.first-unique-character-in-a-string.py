#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # create a dictionary to store the count of each letter
        s_dict = {}
        
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        
        # loop through each letter in the string
        for i in range(len(s)):
            # if the count of the letter is 1, return the index
            if s_dict[s[i]] == 1:
                return i
        
        # if there is no unique letter, return -1
        return -1
        
# @lc code=end

