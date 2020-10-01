'''
Given a set of coin values coins = {c1, c2,..., ck} and a target sum of money n, our task is to
form the sum n using as few coins as possible.
'''

from typing import List

memo = {}
def minCoinRequired(coins: List[int], n: int) -> int:
    if(n < 0):
        return float('inf')
    if(n == 0):
        return 0
    if(n in memo):
        return memo[n]

    minimum = float('inf')
    for coin in coins:
        minimum = min(minimum, minCoinRequired(coins, n-coin)+1)

    if(n not in memo):
        memo[n] = minimum

    return minimum

def minCoinRequiredIterative(coins: List[int], n: int) -> int:
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for x in range(1,n+1):
        for coin in coins:
            if(x-coin >= 0):
                dp[x] = min(dp[x],dp[x-coin]+1)
            print(x,dp)
    return dp[n]


coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
n = 10
# print(minCoinRequired(coins, n))
print(minCoinRequiredIterative(coins, n))

