#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = []
        current_len = 0
        max_len = 0
        
        for char in s:
            # Check if char is in seen_chars
            if char in seen_chars:
                # Check if current_len is greater than max_len
                if current_len > max_len:
                    max_len = current_len
                # Remove all chars before the first occurence of char
                seen_chars = seen_chars[seen_chars.index(char)+1:]
                # Update current_len
                current_len = len(seen_chars)
            
            # Add char to seen_chars
            seen_chars.append(char)
            # Update current_len
            current_len += 1
        
            # Check if current_len is greater than max_len
            if current_len > max_len:
                max_len = current_len
        
        return max_len    
        
# @lc code=end

