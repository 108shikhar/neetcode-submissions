class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(0,len(nums),1):
            x=nums[i]
            if x not in d:
                d[x]=1
            if x in d:
                d[x]=d[x]+1
        d2=sorted(d.items(), key=lambda item: item[1], reverse=True)
        l=[]
        for key, value in d2:
            l.append(key)
        l2=[]
        for i in range(0,k,1):
            l2.append(l[i])
        return l2