class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=[]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                add=nums[i]+nums[l]+nums[r]
                if add==0:
                    a.append([nums[i],nums[l],nums[r]])
                    l,r=l+1,r-1
                    while l<r and nums[l]==nums[l-1]:
                        l=l+1
                    while l<r and nums[r]==nums[r+1]:
                        r=r-1
                elif add>0:
                    r=r-1
                elif add<0:
                    l=l+1
        return a    