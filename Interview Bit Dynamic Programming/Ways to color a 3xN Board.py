import sys
sys.setrecursionlimit(100)
class Solution:
    def func(self,arr,n,m):
        if n==1:
            return arr
        if n%2==0:
            arr=self.func(arr,n//2,m)
            arr=[[(arr[0][0]*arr[0][0]+arr[0][1]*arr[1][0])%m,(arr[0][0]*arr[0][1]+arr[0][1]*arr[1][1])%m],
                 [(arr[1][0]*arr[0][0]+arr[1][1]*arr[1][0])%m,(arr[1][0]*arr[0][1]+arr[1][1]*arr[1][1])%m]]
            return arr
        if n%2==1:
            arr=self.func(arr,n//2,m)
            arr=[[(arr[0][0]*arr[0][0]+arr[0][1]*arr[1][0])%m,(arr[0][0]*arr[0][1]+arr[0][1]*arr[1][1])%m],
                 [(arr[1][0]*arr[0][0]+arr[1][1]*arr[1][0])%m,(arr[1][0]*arr[0][1]+arr[1][1]*arr[1][1])%m]]
            arr=[[(arr[0][0]*11+arr[0][1]*10)%m,(arr[0][0]*5+arr[0][1]*7)%m],
                 [(arr[1][0]*11+arr[1][1]*10)%m,(arr[1][0]*5+arr[1][1]*7)%m]]
            return arr
    def solve(self, n):
        m=10**9+7
        if n==1:
            return 36
        arr=[ [11,5],[10,7]]
        #print(arr[1][1])
        if n>1:
            arr=self.func(arr,n-1,m)
        ans=24*arr[0][0]+12*arr[1][0]+24*arr[0][1]+12*arr[1][1]
        #print(arr)
        return ans%m
