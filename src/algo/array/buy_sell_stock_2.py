# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = profit + (prices[i] - prices[i-1])

        return profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     l = 0
    #     r = 1
    #     result = 0

    #     while r < len(prices):
    #         # print(f"r >>> {r}")
    #         if prices[r] < prices[r-1]:
    #             if prices[r-1] > prices[l]:
    #                 profit = prices[r-1] - prices[l]
    #                 result = result + profit
    #             l = r
    #         elif prices[r] >= prices[r-1] and r == len(prices)-1:
    #             # print("yes")
    #             profit = prices[r] - prices[l]
    #             result = result + profit

    #         r += 1

    #     return result     