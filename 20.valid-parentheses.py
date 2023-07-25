#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack
        stack = []

        # create a dictionary of valid parentheses
        valid_parentheses = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        # loop through each character in the string
        for char in s:
            # if the character is a closing bracket
            if char in valid_parentheses:
                # pop the last item from the stack
                top_element = stack.pop() if stack else '#'
                
                # if the popped item is not the corresponding opening bracket
                if valid_parentheses[char] != top_element:
                    return False
            # if the character is an opening bracket
            else:
                # push the character to the stack
                stack.append(char)
                
        # if the stack is empty, return True
        # else, return False
        return not stack
        
# @lc code=end

