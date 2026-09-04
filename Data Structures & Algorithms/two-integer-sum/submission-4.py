class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            x=nums[i]
            y=target-x
            if y in nums:
                k=nums.index(y)
                if k!=i and k<i:
                    a=[]
                    a.append(k)
                    a.append(i)
                    return a
                elif k!=i and k>i:
                    a=[]
                    a.append(i)
                    a.append(k)
                    return a