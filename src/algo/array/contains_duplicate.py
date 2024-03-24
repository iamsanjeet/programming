#  https://leetcode.com/problems/contains-duplicate/

class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)

        for i in range(size):
            for j in range(i+1, size):
                if nums[i] == nums[j]:
                    return True
        
        return False

    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()
    #     for i in range(1, len(nums)):
    #         if nums[i] == nums[i-1]:
    #             return True
    #     return False

    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     cache = {}

    #     for num in nums:
    #         if cache.get(num):
    #             return True
    #         else:
    #             cache[num] = True
        
    #     return False
        