"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

def coinChange(self, coins, amount):
        minCoins = [0]*(amount+1)
        if amount ==0: return 0
        if all(i> amount for i in coins): return -1
        if len(coins) == 1:
            if amount % coins[0] == 0: return amount/coins[0]
            else: return -1
        for i in range(1,amount+1):
            minCoins[i] =  float("inf")
            for m in coins:
                if m<= i:
                    total = minCoins[i-m] + 1
                    if total <= minCoins[i]:
                        minCoins[i] = total

        if minCoins[amount] == float("inf"): return -1
        else: return minCoins[amount]
