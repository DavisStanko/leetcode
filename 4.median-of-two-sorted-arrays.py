#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            
            # combine the two lists
            nums3 = nums1 + nums2
    
            # sort the combined list
            nums3.sort()
    
            # find the median
            if len(nums3) % 2 == 0:
                return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2
            else:
                return nums3[len(nums3) // 2]
        
# @lc code=end

