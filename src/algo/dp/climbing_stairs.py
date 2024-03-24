class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]
    # def climbStairs(self, n: int) -> int:
    #     left, right = 1, 1

    #     for i in range(n-1):
    #         temp = left
    #         left = left + right
    #         right = temp
        
    #     return left
    # def climb(self, cache, n):
    #     if n == 1 or n == 0:
    #         return 1
        
    #     if cache.get(n) is not None:
    #         return cache.get(n)

    #     opt1 = self.climb(cache, n-1)
    #     opt2 = self.climb(cache, n-2)
    #     cache[n-1] = opt1
    #     cache[n-2] = opt2

    #     return opt1 + opt2

    # def climbStairs(self, n: int) -> int:
        # options - 1 or 2
        # total - n
        # distinct path

        paths = 0
        cache = {}
        result = self.climb(cache, n)

        return result