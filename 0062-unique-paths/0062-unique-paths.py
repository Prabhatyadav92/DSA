class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                dp[j]=dp[j]+dp[j-1]
        return dp[n-1]



        # k=m-n

        # if m==n:
        #     return m*(n-1)
        # if m>n:
        #     return abs(k*m)
        # return abs(k*n)
   
           
        