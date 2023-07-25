#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # Replace the number with the sum of the squares of its digits
        # Repeat until the number equals 1 (where it will stay)

        # create a set to store the numbers
        seen = set()
        
        # loop until the number equals 1
        while n != 1:
            # if the number is in the set, return False
            if n in seen:
                return False
            # add the number to the set
            seen.add(n)
            # replace the number with the sum of the squares of its digits
            n = sum(int(i) ** 2 for i in str(n))
        
        return True
        
# @lc code=end

