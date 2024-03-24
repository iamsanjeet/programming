# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = end = 0
        result = 0

        cache = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

        for end in range(len(s)):
            cache[s[end]] += 1
            window = end-start+1
            max_repeat_char = max(cache.values())

            while window - max_repeat_char > k:
                cache[s[start]] -= 1
                start += 1
                window = end-start+1
        
            result = max(result, window)

        return result






        