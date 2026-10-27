class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # number of ships is number of days
        low,high=max(weights),sum(weights)
        ans=high
        def port(n):
            ships,capacity=1,n
            for w in weights:
                if capacity-w < 0:
                    ships=ships+1
                    capacity=n
                capacity=capacity-w
            return ships
        while low<=high:
            mid=(low+high)//2
            if port(mid)<=days:
                ans=min(ans,mid)
                high=mid-1
            elif port(mid)>days:
                low=mid+1
        return ans