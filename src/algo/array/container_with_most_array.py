# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0

        while l < r:
            lt = r - l
            ht = height[r] if height[l] > height[r] else height[l]
            # print(f"l - {l}, r - {r}, lt - {lt}, ht - {ht}, area - {lt*ht}")
            area = max(area, lt * ht)

            if height[l] < height[r]:
                l = l + 1
            else:
                r = r -1
            # print(f"adjusted pointers. l - {l}, r - {r}")
        
        return area
        