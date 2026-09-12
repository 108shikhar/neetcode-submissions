class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m=len(s1)
        n=len(s2)
        p=len(s3)
        dp=[[None for c in range(n+1)] for r in range(m+1)]
        i,j=m,n
        def solve(i,j):
            if m + n != p:
                return False
            if i==0 and j==0:
                return True
            if dp[i][j]!=None:
                return dp[i][j]
            x=i+j-1
            one=False
            two=False
            if i>0 and s3[x]==s1[i-1]:
                one=solve(i-1,j)
            elif j>0 and s3[x]==s2[j-1]:
                two=solve(i,j-1)
            dp[i][j]=one or two
            return dp[i][j]
        return solve(i,j)