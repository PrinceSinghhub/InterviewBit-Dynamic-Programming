from sys import setrecursionlimit as st
st(10**8)
class Solution:
    def solve(seld, A):
        dp = [1] * (A + 32)
        total = 62
        dp[1] = 2
        dp[2] = 4
        dp[3] = 8
        dp[4] = 16
        dp[5] = 32
        for x in range(6, A):
            dp[x] = (total + 1)
            total += dp[x]
            total -= dp[x - 6]
            total %= (10 ** 9 + 7)
            dp[x] %= (10 ** 9 + 7)
       # print(dp)
        return dp[A-1]
