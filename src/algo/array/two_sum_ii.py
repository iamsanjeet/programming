class Solution:
    # Complexity - O(n), space complexity - O(n)
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     cache = {}
    #     for i, num in enumerate(numbers):
    #         rem = target - num

    #         if cache.get(rem) is not None:
    #             return [cache.get(rem) + 1, i + 1]
    #         else:
    #             cache[num] = i

    # Complexity - O(n), space complexity - O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        # print(f"Initialize. l - {l}, r - {r}")

        while l < r:
            if numbers[l] + numbers[r] > target:
                r = r - 1
                # print(f"r decreased to - {r}")
            elif numbers[l] + numbers[r] < target:
                l = l + 1
                # print(f"l increased to - {l}")
            else:
                return [l+1, r+1]
        