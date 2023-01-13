class Solution:
    # @param A : list of list of integers
    # @return an integer
    import sys
    def solve(self, A):
        l = len(A)
        from bisect import bisect_left
        arr = [-sys.maxsize] * (l + 1)
        cl = 0
        cm = -sys.maxsize
        # A.sort()
        for i in A:
            if i[0] > arr[cl]:
                cl += 1
                arr[cl] = i[1]
            else:
                x = bisect_left(arr, i[0], 0, cl + 1)
                if x <= l and arr[x] > i[1]:
                    arr[x] = i[1]

        return cl



