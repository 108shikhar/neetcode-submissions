class Solution:
    def numDecodings(self, s: str) -> int:
        i=1
        j=0
        d={}
        x='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while j<len(x):
            d[x[j]]=i
            i=i+1
            j=j+1
        i=0
        dp=[None for j in range(100)]
        def solve(i):
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            if i==len(s)-1:
                return 1
            if dp[i]!=None:
                return dp[i]
            dp[i] = solve(i+1)
            if int(s[i:i+2])<=26:
                dp[i] = dp[i] + solve(i+2)
            return dp[i]
        return solve(i)