#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
            
            # create a set for each list
            set1 = set(nums1)
            set2 = set(nums2)
    
            # return the intersection of the two sets
            return set1.intersection(set2)
        
# @lc code=end

