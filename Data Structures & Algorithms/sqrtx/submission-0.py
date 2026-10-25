class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==0:
            return x
        else:
            l,h=1,x//2
            dif,ans=0,0
            while l<=h:
                m=(l+h)//2
                val=m*m
                dif=val-x
                if dif==0:
                    return m
                elif dif<0:
                    ans=m
                    l=m+1
                elif dif>0:
                    h=m-1
            return ans