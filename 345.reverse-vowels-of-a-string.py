#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # convert string to list
        s = list(s)
        
        # create a list of vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        # create a list of vowels in the string
        string_vowels = []
        
        for i in s:
            if i.lower() in vowels:
                string_vowels.append(i)
        
        # reverse the list of vowels
        string_vowels.reverse()
        
        # replace the vowels in the string with the reversed vowels
        for i in range(len(s)):
            if s[i].lower() in vowels:
                s[i] = string_vowels.pop(0)
        
        # convert the list back to a string
        return ''.join(s)
        
# @lc code=end

