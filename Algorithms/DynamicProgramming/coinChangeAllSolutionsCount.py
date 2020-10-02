'''
The coin change problem where our task is to calculate the total number of ways to produce a sum x using the coins. For
example, if coins = {1,3,4} and x = 5, there are a total of 6 ways:
• 1+1+1+1+1
• 1+1+3
• 1+3+1
• 3+1+1
• 1+4
• 4+1
'''

from typing import List


def coinChange(coins: list, n: int) -> int:
    row = len(coins)+1
    dp = [[0]*(n+1) for x in range(row)]
    dp[0][0] = 1
    for x in range(1,row):
        dp[x][0] = 1
        for y in range(1,n+1):
            if(coins[x-1]>y):
                dp[x][y] = dp[x-1][y]
            else:
                dp[x][y] = dp[x-1][y]+dp[x][y-coins[x-1]]

    return dp[row-1][n]

coins = [1,2,3]
n = 4
print(coinChange(coins,n))