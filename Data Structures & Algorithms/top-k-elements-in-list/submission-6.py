class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d,ans,val={},{},[]
        for i in nums:
            if i not in d:
                d[i]=1
            elif i in d:
                d[i]=d[i]+1
        ans=sorted(d.items(), key=lambda x: x[1], reverse=True)
        for key, value in ans:
            val.append(key)
            if len(val)==k:
                return val