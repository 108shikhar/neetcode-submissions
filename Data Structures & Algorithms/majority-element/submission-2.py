class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m,d=len(nums)/2,{}
        maximum,output=0,0
        for i in nums:
            if i not in d:
                d[i]=1
            elif i in d:
                d[i]=d[i]+1
        for key, value in d.items():
            if d[key]>m:
                maximum=max(maximum,d[key])
                output=key
        return output