class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            # To remove duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - num

            l = i + 1
            r = len(nums) -1

            while l < r:
                if nums[l] + nums[r] > target:
                    r = r -1
                elif nums[l] + nums[r] < target:
                    l = l + 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l = l +1
        return result

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     result = []
    #     size = len(nums)

    #     for i in range(size):
    #         # print(f"current i - {i}. result - {result}")
    #         if i > 0 and nums[i] == nums[i-1]:
    #             # print(f"duplicate i, skip")
    #             continue
    #         # print(f"result before j loop - {result}")

    #         balance = 0 - nums[i]

    #         cache = {}
    #         prev = None
    #         for j in range(i+1, size):
    #             rem = balance - nums[j]

    #             if cache.get(rem) is not None:
    #                 new = [nums[i], nums[cache.get(rem)], nums[j]]
    #                 if prev and new == prev:
    #                     print(f"new sol {new} is same as prev sol {prev}")
    #                 else: 
    #                     result.append(new)
    #                     prev = new
    #             else:
    #                 cache[nums[j]] = j
            
    #         cache = {}
        
    #     return result



        