class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        ans=r
        while l<=r:
            m=(l+r)//2
            hour=0
            for b in piles:
                hour=hour+math.ceil(b/m)
            if hour<=h:
                r=m-1
                ans=m
            elif hour>h:
                l=m+1
        return ans