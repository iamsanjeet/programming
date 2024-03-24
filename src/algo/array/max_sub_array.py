# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum = curr_sum + num

            if curr_sum > max_sum:
                max_sum = curr_sum
            

            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         curr_sum = None
#         max_sum = None

#         if len(nums) == 1:
#             return nums[0]

#         for i in range(len(nums)):
#             curr_sum = curr_sum + nums[i] if curr_sum is not None else nums[i]

#             if nums[i] > curr_sum:
#                 curr_sum = nums[i]
#                 max_sum = curr_sum


#             if curr_sum <= 0:
#                 curr_sum = 0
#                 max_sum = max(max_sum, nums[i]) if max_sum is not None else nums[i]
            
#             if curr_sum > 0:
#                 max_sum = max(curr_sum, max_sum) if max_sum is not None else nums[i]
            
        
#         return max_sum


            
        