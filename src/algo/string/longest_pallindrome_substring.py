class Solution:
    def is_pallindrome(self, s):
        start = 0
        end = len(s) -1

        while start < end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        
        return True

    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        result = ""

        for i in range(size):
            for j in range(i+1, size):
                sub_arr = s[i:j]

                if self.is_pallindrome(sub_arr):
                    if len(sub_arr) > len(result):
                        result = sub_arr
        
        return result
            




    # def longestPalindrome(self, s: str) -> str:
    #     result = ""
    #     size = len(s)
    #     for i in range(size):
    #         l, r = i, i

    #         # Odd length
    #         while l >= 0 and r <= size -1 and s[l] == s[r]:
    #             pal_len = r - l + 1

    #             if pal_len > len(result):
    #                 result = s[l:r+1]

    #             l -= 1
    #             r += 1
            
    #         # even length
    #         l, r = i, i+1
    #         while l >= 0 and r <= size -1 and s[l] == s[r]:
    #             pal_len = r - l + 1

    #             if pal_len > len(result):
    #                 result = s[l:r+1]

    #             l -= 1
    #             r += 1
        
    #     return result


        