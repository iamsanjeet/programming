class Solution:
    def countPal(self, s, l, r):
        size = len(s)
        count = 0
        while l >= 0 and r <= size -1 and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        return count

    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            # Odd length
            result += self.countPal(s, i, i)
            # Even length
            result += self.countPal(s, i, i + 1)
        
        return result



    # count = 0
    # def countSubstrings(self, s: str) -> int:
    #     size = len(s)
    #     count = 0

    #     for i in range(size):
    #         # odd length
    #         l, r = i, i

    #         while l >= 0 and r <= size -1 and s[l] == s[r]:
    #             count += 1
    #             l -= 1
    #             r += 1

    #         # even length
    #         l, r = i, i+1

    #         while l >= 0 and r <= size -1 and s[l] == s[r]:
    #             count += 1
    #             l -= 1
    #             r += 1
        
    #     return count
        