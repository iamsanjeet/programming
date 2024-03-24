# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = max(nums)

        for num in nums:
            if num == 0:
                curMax = 1
                curMin = 1
            tmp = curMax
            curMax = max(curMax * num, num, curMin * num)
            curMin = min(tmp * num, num, curMin * num)
            res = max(res, curMax, curMin)
        
        return res



        