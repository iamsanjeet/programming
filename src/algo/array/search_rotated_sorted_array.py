# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while r >= l:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid


            # left sorted array
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted array
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1
        return -1


    # def search(self, nums: List[int], target: int) -> int:
    #     i = 0
    #     j = len(nums) -1

    #     while j >= i:
    #         mid = (i+j) // 2

    #         if nums[mid] == target:
    #             return mid
    #         if nums[i] == target:
    #             return i
    #         if nums[j] == target:
    #             return j
            
    #         if nums[mid] > target and nums[mid] > nums[j] and target > nums[j]:
    #             j = mid -1
    #         elif nums[mid] > target and nums[mid] < nums[j] and target < nums[j]:
    #             j = mid -1
    #         elif nums[mid] < target and nums[mid] < nums[j] and target > nums[j]:
    #             j = mid -1
    #         else:
    #             i = mid + 1
        
    #     return -1


        