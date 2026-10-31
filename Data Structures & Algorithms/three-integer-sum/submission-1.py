class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target,a=0,[]
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            val=target-nums[i]
            while l<r:
                add=nums[l]+nums[r]
                if add==val:
                    b=[nums[i],nums[l],nums[r]]
                    if b not in a:
                        a.append(b)
                    l,r=l+1,r-1
                elif add>val:
                    r=r-1
                elif add<val:
                    l=l+1
        return a
                    