# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        i = 0
        j = len(nums) -1

        while j >= i:

            # Condition for sorted array. If array/sub-array is sorted
            if nums[j] > nums[i]:
                result = min(result, nums[i])
                break

            mid = int((i+j)/2)
            result = min(result, nums[mid])

            if nums[mid] >= nums[i]:
                i = mid + 1
            else:
                j = mid - 1
        
        return result

        
