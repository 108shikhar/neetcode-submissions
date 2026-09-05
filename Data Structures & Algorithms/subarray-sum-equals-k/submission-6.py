class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        add=0
        res=0
        for i in range(0, len(nums), 1):
            add=add+nums[i]
            diff=add-k
            if diff in d:
                new=d[diff]
                res=res+new
            if add not in d:
                d[add]=1
            else:
                d[add]=d[add]+1
        return res
        """
        value=0
        for i in range(0, len(nums), 1):
            j=i
            sum=0
            while j<len(nums):
                sum=sum+nums[j]
                if sum==k:
                    value=value+1
                j=j+1
        return value
        """