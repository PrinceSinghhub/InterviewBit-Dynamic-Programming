class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        r,b,g=0,0,0
        lr,lb,lg=A[0][0],A[0][1],A[0][2]
        for i in range(1,len(A)):
            if lb<lg:
                r+=A[i][0]+lb
            else:
                r+=A[i][0]+lg
            if lr<lg:
                b+=A[i][1]+lr
            else:
                b+=A[i][1]+lg
            if lr<lb:
                g+=A[i][2]+lr
            else:
                g+=A[i][2]+lb
            lr,lb,lg=r,b,g
            r,b,g=0,0,0
        return min(lr,lb,lg)
