#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create a new string
        new_string = ''
        
        # loop through each character in the string
        for char in s:
            # if the character is alphanumeric
            if char.isalnum():
                # add the character to the new string
                new_string += char.lower()
        
        # check if the new string is a palindrome
        return new_string == new_string[::-1]
        
# @lc code=end

