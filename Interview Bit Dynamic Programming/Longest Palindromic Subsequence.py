class Solution:
    # @param A : string
    # @return an integer
    def solve(self, s):
        n = len(s);
        dp = [0]*n;

        for i in range(n-1, -1, -1):
            new_dp =  dp[:]
            dp[i] = 1
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[j] = new_dp[j-1] + 2
                elif dp[j-1] > dp[j]:
                    dp[j] = dp[j-1]
        return dp[-1]

