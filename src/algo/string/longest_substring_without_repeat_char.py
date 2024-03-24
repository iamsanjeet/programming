class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        result = 0

        
        left = 0
        charSet = set()

        for right in range(size):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            result = max(result, right-left + 1)

            

        return result



        