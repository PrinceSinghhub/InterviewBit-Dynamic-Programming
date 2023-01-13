MOD = 1000000007


def catalan(n):
    num = 1
    den = 1
    for i in range(2, n + 1):
        num *= (n + i)
        den *= i
    return (num // den) % MOD


class Solution:
    def chordCnt(self, A):
        return catalan(A)

# long long catalan(int n)
# {
#     long long num=1, den=1;
#     for(int i=2; i<=n; i++)
#     {
#         num*=(n+i);
#         den*=i;
#     }
#     return (num/den)%MOD;
# }

# int Solution::chordCnt(int A) {
#     return catalan(A);
# }
