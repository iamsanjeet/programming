# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solutions:
    def maxProfit3(self, prices: list[int]) -> int:
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1


    # Solution2:
    def maxProfit2(self, prices: list[int]) -> int:
        buy = -1
        sell = -1
        profit = 0

        for i in range(len(prices)):
            if buy == -1:
                buy = prices[i]
                print(f"buy set to {buy}")
                continue
            
            if sell == -1:
                if prices[i] > buy:
                    sell = prices[i]
                    profit = max(profit, sell-buy)
                    print(f"sell::set:: profit now is: {profit}")
                else:
                    buy = prices[i]
                    print(f"sell not set bcoz value {prices[i]} is lower than buy. So setting it in buy - {buy}")
                continue

            if prices[i] > sell:
                sell = prices[i]
                profit = max(profit, sell - buy)
                print(f"max sell::set:: profit now is: {profit}")
            elif prices[i] < buy:
                buy = prices[i]
                sell = -1
        
        return profit

    # Solution1: Brute force - O(n2)
    def maxProfit1(self, prices: list[int]) -> int:
        profit = 0
        size = len(prices)

        for i in range(size):
            for j in range(i+1, size):
                profit = max(profit, prices[j]-prices[i])
        
        return profit


# Import the unittest module to create and run unit tests
import unittest

class TestSolutions(unittest.TestCase):
    def setUp(self):
        """Method called to prepare the test fixture."""
        self.runner = Solutions()

    def test_case1(self):
        prices = [7,1,5,3,6,4]
        expected = 5
        self.assertEqual(self.runner.maxProfit3(prices), expected)


# Check if this script is run as the main program and run the tests
if __name__ == '__main__':
    unittest.main()
