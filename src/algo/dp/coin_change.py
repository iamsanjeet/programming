class Solution:

    def min_coins(self, coins: List[int], amount: int, cache: dict):
        ans = float('inf')

        if amount == 0:
            return 0
        
        if cache.get(amount) is not None:
            return cache.get(amount)

        for coin in coins:
            if amount - coin >= 0:
                ans = min(ans, 1 + self.min_coins(coins, amount - coin, cache))
            else:
                ans = min(ans,float('inf'))
        
        cache[amount] = ans
        
        return ans
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        result = self.min_coins(coins, amount, cache)

        return result if result != float('inf') else -1


    # # o(m^n) -> brute force
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     ans = float('inf')

    #     if amount == 0:
    #         return 0

    #     for coin in coins:
    #         if amount - coin >= 0:
    #             ans = min(ans, 1 + self.coinChange(coins, amount - coin))
    #         else:
    #             return float('inf')
        
    #     return ans if ans != float('inf') else -1



    # greedy
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     coins.sort(reverse=True)
    #     max_coin_index = 0
    #     max_coin = coins[max_coin_index]
    #     sum = amount
    #     count = 0

    #     while sum > 0:
    #         print(f"sum - {sum}, max coin - {max_coin}, max index - {max_coin_index}")
    #         if sum - max_coin >= 0:
    #             count+= 1
    #             sum = sum - max_coin
    #             print(f"updated sum - {sum}, updated count - {count}")
    #         elif max_coin_index == len(coins)-1:
    #             return -1
    #         else:
    #             max_coin_index += 1
    #             max_coin = coins[max_coin_index]
        
    #     return count





    # dp
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp = [float('inf')] * (amount+1)
    #     dp[0] = 0
        
    #     for i in range(1, amount + 1):
    #         for c in coins:
    #             if i -c >= 0:
    #                 dp[i] = min(dp[i], 1 + dp[i-c])
        
    #     return dp[amount] if dp[amount] != float('inf') else -1
        