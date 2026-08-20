class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        for i in range(0, len(nums), 1):
            n=nums[i]
            if n not in d:
                d[n]=1
            elif n in d:
                d[n]=d[n]+1
        p=[]
        q=int(len(nums)//3)
        for key, value in d.items():
            if d[key]>q:
                p.append(key)
        return p