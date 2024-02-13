class Solutions:
    # Approach 1: Brute force   O(n2)
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        return None

    # Appraoch 2: Optimized O(n)
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        cache = {}

        for i,num in enumerate(nums):
            target_remain = target - num

            if cache.get(target_remain) is not None:
                return [cache.get(target_remain), i]
            cache[num] = i


# Import the unittest module to create and run unit tests
import unittest

class TestSolutions(unittest.TestCase):
    def setUp(self):
        """Method called to prepare the test fixture."""
        self.runner = Solutions()

    def test_case1(self):
        nums = [2,7,11,15]
        target = 9
        expected = [0,1]
        self.assertEqual(self.runner.twoSum1(nums, target), expected)


# Check if this script is run as the main program and run the tests
if __name__ == '__main__':
    unittest.main()
