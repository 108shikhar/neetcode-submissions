class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        ans=0
        for r in range(len(s)):
            x=s[r]
            if x in d:
                d[x]=d[x]+1
            elif x not in d:
                d[x]=1
            while ( (r-l+1)-max(d.values()) ) > k:
                y=s[l]
                d[y]=d[y]-1
                l=l+1
            ans=max(ans,(r-l+1))
        return ans