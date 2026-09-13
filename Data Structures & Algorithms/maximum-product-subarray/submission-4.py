class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=nums[0]
        minimum=nums[0]
        ans=nums[0]
        for i in range(1,len(nums),1):
            x=nums[i]
            big=max(x,(maximum*x),(minimum*x))
            small=min(x,(maximum*x),(minimum*x))
            ans=max(maximum,big,ans)
            maximum=big
            minimum=small
        return ans