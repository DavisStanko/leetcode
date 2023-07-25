#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            
            # if the target is in the list, return the index
            if target in nums:
                return nums.index(target)
            
            # if the target is not in the list, append it to the list
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)
        
# @lc code=end

