#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # map roman to integer
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # convert string to list
        s = list(s)
        
        # convert roman to integer
        for i in s:
            s[s.index(i)] = roman_map[i]
        
        # do the math
        answer = 0
        
        # if the next number is greater than the current number, subtract the current number
        # else, add the current number
        for i in range(len(s)):
            if i < len(s) - 1 and s[i] < s[i + 1]:
                answer -= s[i]
            else:
                answer += s[i]
        
        return answer
        
        
# @lc code=end

