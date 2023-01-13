class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        dp = [[0]*(len(A)+1) for _ in range(len(A)+1)]
        for i in range(1,len(A)+1):
            for j in range(1,len(A)+1):
                if A[i-1]==A[j-1] and i!=j: dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if(dp[i][j]>=2): return(1)
        return(0)
        # d={}
        # for i in range(len(A)):
        #     for j in range(i+1,len(A)):
        #         d[(i,j)] = A[i]+A[j]
        # for key,val in d.items():
        #     for k,v in d.items():
        #         if(key!=k and key[0]!=k[0] and key[1]!=k[1] and val == v):
        #             return(1)
        # return(0)
