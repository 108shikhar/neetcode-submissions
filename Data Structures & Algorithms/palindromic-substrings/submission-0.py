class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            #odd
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                ans=ans+1
                l=l-1
                r=r+1
            #even
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                ans=ans+1
                l=l-1
                r=r+1
        return ans