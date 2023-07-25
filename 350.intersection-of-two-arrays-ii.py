#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            
            # create a dictionary to store the count of each number in nums1
            nums1_dict = {}
    
            for i in nums1:
                if i in nums1_dict:
                    nums1_dict[i] += 1
                else:
                    nums1_dict[i] = 1
    
            # create a list to store the common numbers
            common_nums = []
    
            # loop through each number in nums2
            for i in nums2:
                # if the number is in nums1_dict and the count is greater than 0
                if i in nums1_dict and nums1_dict[i] > 0:
                    # add the number to the common_nums list
                    common_nums.append(i)
                    # decrement the count of the number in nums1_dict
                    nums1_dict[i] -= 1
    
            return common_nums
        
# @lc code=end

