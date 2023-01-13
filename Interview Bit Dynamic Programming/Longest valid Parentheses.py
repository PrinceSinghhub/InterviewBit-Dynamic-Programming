class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        l, r = 0, 0
        mx = 0
        for p in A:
            if p == '(':
                l += 1
            else:
                r += 1
            if l == r:
                mx = max(mx, 2 * r)
            elif r > l:
                l, r = 0, 0
        l, r = 0, 0

        for s in reversed(A):
            if s == ')':
                r += 1
            else:
                l += 1
            if l == r:
                mx = max(mx, 2 * r)
            elif l > r:
                l, r = 0, 0
        return mx

