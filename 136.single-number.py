#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # create a dictionary to store the number of occurrences of each number
        num_dict = {}
        
        # loop through each number
        for num in nums:
            # if the number is not in the dictionary
            if num not in num_dict:
                # add the number to the dictionary
                num_dict[num] = 1
            # if the number is in the dictionary
            else:
                # increment the number of occurrences
                num_dict[num] += 1
        
        # loop through each key in the dictionary
        for key in num_dict:
            # if the number of occurrences is 1
            if num_dict[key] == 1:
                # return the number
                return key
        
        # return None
        return None
        
# @lc code=end

