class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans,dp=0,{}
        l,r=0,0
        while r<len(s):
            x=s[r]
            if x not in dp:
                dp[x]=r
            elif x in dp:
                l=max(l,dp[x]+1)
                dp[x]=r
            ans=max(ans,r-l+1)
            r=r+1
        return ans