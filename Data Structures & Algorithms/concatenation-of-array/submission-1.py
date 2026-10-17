class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n,ans=len(nums),[]
        for i in range(2):
            for j in range(n):
                ans.append(nums[j])
        return ans