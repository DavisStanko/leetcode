#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # get shortest string
        test_word = min(strs, key=len)
        
        # loop through each letter in the shortest string
        for i in range(len(test_word)):
            # check if the letter is in each string
            for word in strs:
                if word[i] != test_word[i]:
                    return test_word[:i]
        
        return test_word
            
        
                
                
        
# @lc code=end

