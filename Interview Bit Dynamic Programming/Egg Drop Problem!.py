def bi(x,n):
    s,term,i = 0,1,1
    while i <=n:
        term *= (x-i+1)/i
        s += term
        i += 1
    return s


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        l,r = 1,B
        while l <r:
            mid = (l+r)//2
            if bi(mid,A) < B:
                l = mid+1
            else:
                r = mid
        return l
