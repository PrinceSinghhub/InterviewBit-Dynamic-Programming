class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l = sum(A)
        b =1
        for i in A:
            b|=(b<<i)
        k = bin(b)[2:]
        k =k[::-1]
        mid = len(k)//2
        ans =float("inf")
        for j in range(l//2,-1,-1):
            if k[j]=="1":
                ans = min(ans,l-2*j)
                break
        return ans
