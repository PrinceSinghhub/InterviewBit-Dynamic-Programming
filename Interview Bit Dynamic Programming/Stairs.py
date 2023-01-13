class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A, memo={}):
        if A == 0 or A == 1:
            return 1

        if A in memo:
            return memo[A]

        n_th_fibo = (self.climbStairs(A-1, memo)+self.climbStairs(A-2, memo))
        memo[A] = n_th_fibo

        return n_th_fibo


