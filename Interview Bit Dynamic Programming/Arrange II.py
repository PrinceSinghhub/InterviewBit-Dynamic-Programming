class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, B):

        if (len(A) < B):
            return -1
        array = []
        sums = 1
        i = 1
        while (i < len(A)):
            if (A[i] != A[i - 1]):
                array.append(sums)
                sums = 1
            else:
                sums += 1
            i += 1
        array.append(sums)

        cumm = [[0, 0] for x in range(len(array) + 1)]
        i = 1
        while (i < len(cumm)):
            if (i % 2 == 0):
                cumm[i][0] = cumm[i - 1][0] + array[i - 1]
                cumm[i][1] = cumm[i - 1][1]
            else:
                cumm[i][0] = cumm[i - 1][0]
                cumm[i][1] = cumm[i - 1][1] + array[i - 1]
            i += 1

        # print(array)
        # print(cumm)
        dp = [[0 for x in range(len(array))] for y in range(B)]
        i = 0
        while (i < len(dp)):
            j = i
            while (j < len(dp[0])):
                if (i == 0):
                    dp[i][j] = self.prod(i, j, cumm)
                else:
                    k = i - 1
                    minm = 2 ** 31 - 1
                    while (k < j):
                        ans = dp[i - 1][k] + self.prod(k + 1, j, cumm)
                        # print(k,j,ans)
                        if (ans < minm):
                            minm = ans
                        k += 1
                    dp[i][j] = minm
                j += 1
            i += 1
        # print(dp)
        return dp[B - 1][-1]

    def prod(self, i, j, cumm):
        ans = (cumm[j + 1][0] - cumm[i][0]) * (cumm[j + 1][1] - cumm[i][1])
        return ans

