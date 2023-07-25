#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a dictionary to store the count of each letter in magazine
        magazine_dict = {}
        
        for i in magazine:
            if i in magazine_dict:
                magazine_dict[i] += 1
            else:
                magazine_dict[i] = 1
        
        # loop through each letter in ransomNote
        for i in ransomNote:
            # if the letter is in magazine_dict and the count is greater than 0
            if i in magazine_dict and magazine_dict[i] > 0:
                # decrement the count of the letter in magazine_dict
                magazine_dict[i] -= 1
            else:
                return False
        
        return True
        
# @lc code=end

