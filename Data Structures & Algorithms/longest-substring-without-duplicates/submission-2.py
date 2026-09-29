class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        dp={}
        l,r=0,0
        while r in range(len(s)):
            x=s[r]
            if x not in dp:
                dp[x]=r
            elif x in dp:
                l=max(l,dp[x]+1)
                dp[x]=r
            length=r-l+1
            ans=max(ans,length)
            r=r+1
        return ans