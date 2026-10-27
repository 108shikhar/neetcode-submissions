class Solution:
    def findMin(self, nums: List[int]) -> int:
        res,l,h=nums[0],0,len(nums)-1
        while l<=h:
            if nums[l]<nums[h]:
                res=min(res,nums[l])
                break
            m=(l+h)//2
            res=min(res,nums[m])
            if nums[l]<=nums[m]:
                l=m+1
            elif nums[l]>nums[m]:
                h=m-1
        return res