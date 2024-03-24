# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size

        prefix = 1
        for i in range(size):
            result[i] = prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(size-1, -1, -1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]
        
        return result

        


        