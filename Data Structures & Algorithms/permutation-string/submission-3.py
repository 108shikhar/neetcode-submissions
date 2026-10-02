class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        d1={}
        for i in s1:
            if i not in d1:
                d1[i]=1
            elif i in d1:
                d1[i]=d1[i]+1

        d2={}
        for j in s2[:k]:
            if j not in d2:
                d2[j]=1
            elif j in d2:
                d2[j]=d2[j]+1
        if d1==d2:
            return True

        for r in range(k,len(s2),1):
            if s2[r] not in d2:
                d2[s2[r]]=1
            elif s2[r] in d2:
                d2[s2[r]]=d2[s2[r]]+1
            l=s2[r-k]
            d2[l]=d2[l]-1
            if d2[l]==0:
                d2.pop(l)
            if d1 == d2:
                return True

        return False