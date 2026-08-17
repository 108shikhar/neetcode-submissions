class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            elif i in d:
                d[i]=d[i]+1
        """
        m=dict(sorted(d.items(), lambda=value item: item[1], reverse=True))
        """
        maximum=0
        output=0
        for key, value in d.items():
            if value>=maximum:
                maximum=value
                output=key
        return output