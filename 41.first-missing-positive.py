#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Move positive numbers to their correct positions (i.e., nums[i] == i+1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Step 2: Find the first missing positive number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

        
        
# @lc code=end

