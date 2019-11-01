
class Solutions:
    def two_sum(self, nums, target):
        nums.sort()
        start = 0
        end = len(nums) - 1

        while end > start:
            current_sum = nums[start] + nums[end]
            if current_sum == target:
                return [start, end]
            elif current_sum > target:
                end = end - 1
            else:
                start = start + 1
        return None








    #O(n) solution
    # def two_sum(self, nums, target):
    #     num_index_map = {}
    #     for i in range(0, len(nums)):
    #         left = target - nums[i]
    #
    #         if num_index_map.get(left) is not None:
    #             return [num_index_map[left], i]
    #         else:
    #             num_index_map[nums[i]] = i

    #O(n*2) solution
    # def two_sum(self, nums, target):
    #     num_index_map = {}
    #     for i in range(0, len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i,j]
if __name__ == '__main__':
    s = Solutions()
    # Test Case 1
    expected = [0,1]
    actual = s.two_sum([2,7,11,15], 9)
    print(actual)
    assert expected == actual






